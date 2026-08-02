"""
Mustapha Blida AI - FastAPI Backend Server
==========================================
API server for AI video generation pipeline.
"""

import os
import sys
import uuid
import json
from datetime import datetime
from typing import Optional, List
from pathlib import Path

from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field
import uvicorn

# Ensure app directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.config.config import Config
from app.services.video_service import VideoService

# ==================== CONFIG ====================
config = Config()

# ==================== FASTAPI APP ====================
app = FastAPI(
    title="Mustapha Blida AI API",
    description="AI-powered short video generation API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# In-memory task storage (use Redis in production)
tasks = {}

# ==================== MODELS ====================
class VideoRequest(BaseModel):
    video_subject: str = Field(..., description="Topic or keyword for the video")
    video_script: Optional[str] = Field(None, description="Optional custom script")
    video_terms: Optional[List[str]] = Field(None, description="Optional search terms")
    video_aspect: str = Field("9:16", description="Aspect ratio: 9:16, 16:9, or 1:1")
    video_concat_mode: str = Field("random", description="random or sequential")
    video_transition_mode: str = Field("no", description="Transition effect")
    video_clip_duration: int = Field(3, description="Max clip duration in seconds")
    video_count: int = Field(1, description="Number of videos to generate")
    video_language: str = Field("en", description="Video language code")
    voice_name: Optional[str] = Field(None, description="TTS voice name")
    voice_volume: float = Field(1.0, description="Voice volume 0.1-2.0")
    voice_rate: float = Field(1.0, description="Voice speed 0.5-2.0")
    bgm_type: str = Field("random", description="Background music type")
    bgm_volume: float = Field(0.2, description="BGM volume 0.0-1.0")
    subtitle_enabled: bool = Field(True, description="Enable subtitles")
    subtitle_position: str = Field("bottom", description="Subtitle position")
    custom_position: float = Field(0.5, description="Custom Y position")
    font_name: str = Field("default", description="Subtitle font")
    text_fore_color: str = Field("#FFFFFF", description="Text color")
    text_background_color: str = Field("transparent", description="BG color")
    font_size: int = Field(60, description="Font size")
    stroke_color: str = Field("#000000", description="Stroke color")
    stroke_width: float = Field(1.5, description="Stroke width")
    n_threads: int = Field(2, description="Number of threads")
    paragraph_number: int = Field(1, description="Number of paragraphs")
    llm_provider: str = Field("openai", description="LLM provider")
    llm_model_name: str = Field("gpt-4o-mini", description="LLM model")

class ScriptRequest(BaseModel):
    video_subject: str
    video_language: str = "en"
    paragraph_number: int = 1

class TermsRequest(BaseModel):
    video_script: str
    video_language: str = "en"

class TaskResponse(BaseModel):
    task_id: str
    status: str
    message: str
    created_at: str

class TaskStatus(BaseModel):
    task_id: str
    status: str  # pending, processing, completed, failed
    progress: int
    result: Optional[dict] = None
    error: Optional[str] = None
    created_at: str
    updated_at: str

# ==================== ENDPOINTS ====================

@app.get("/")
def root():
    return {
        "app": "Mustapha Blida AI",
        "version": "1.0.0",
        "author": "https://x.com/mouse0000000",
        "docs": "/docs"
    }

@app.post("/api/v1/videos", response_model=TaskResponse)
def create_video(request: VideoRequest, background_tasks: BackgroundTasks):
    """Generate a short video from topic"""
    task_id = str(uuid.uuid4())

    tasks[task_id] = {
        "task_id": task_id,
        "status": "pending",
        "progress": 0,
        "result": None,
        "error": None,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    background_tasks.add_task(_generate_video_task, task_id, request)

    return TaskResponse(
        task_id=task_id,
        status="pending",
        message="Video generation started",
        created_at=tasks[task_id]["created_at"]
    )

@app.get("/api/v1/tasks")
def list_tasks():
    """Get all tasks"""
    return {"tasks": list(tasks.values())}

@app.get("/api/v1/tasks/{task_id}")
def get_task(task_id: str):
    """Query task status"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id: str):
    """Delete a task"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}

@app.post("/api/v1/scripts")
def generate_script(request: ScriptRequest):
    """Generate video script"""
    try:
        service = VideoService(config)
        script = service.generate_script(
            topic=request.video_subject,
            language=request.video_language,
            paragraphs=request.paragraph_number
        )
        return {"script": script}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/terms")
def generate_terms(request: TermsRequest):
    """Generate search terms from script"""
    try:
        service = VideoService(config)
        terms = service.extract_terms(
            script=request.video_script,
            language=request.video_language
        )
        return {"terms": terms}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/musics")
def list_musics():
    """List available background music"""
    music_dir = Path("resource/songs")
    if not music_dir.exists():
        return {"musics": []}
    musics = [f.name for f in music_dir.iterdir() if f.suffix in (".mp3", ".wav")]
    return {"musics": musics}

@app.get("/api/v1/stream/{file_path:path}")
def stream_video(file_path: str):
    """Stream video file"""
    full_path = Path(file_path)
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return StreamingResponse(open(full_path, "rb"), media_type="video/mp4")

@app.get("/api/v1/download/{file_path:path}")
def download_video(file_path: str):
    """Download video file"""
    full_path = Path(file_path)
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(full_path, media_type="video/mp4", filename=full_path.name)

# ==================== BACKGROUND TASK ====================
def _generate_video_task(task_id: str, request: VideoRequest):
    """Background video generation"""
    tasks[task_id]["status"] = "processing"
    tasks[task_id]["updated_at"] = datetime.now().isoformat()

    try:
        service = VideoService(config)

        # Stage 1: Script
        tasks[task_id]["progress"] = 10
        script = request.video_script or service.generate_script(
            request.video_subject, request.video_language, request.paragraph_number
        )

        # Stage 2: Terms
        tasks[task_id]["progress"] = 20
        terms = request.video_terms or service.extract_terms(script, request.video_language)

        # Stage 3: Footage
        tasks[task_id]["progress"] = 40
        clips = service.fetch_footage(terms, request.video_clip_duration)

        # Stage 4: Voiceover
        tasks[task_id]["progress"] = 60
        audio = service.generate_voiceover(script, request.voice_name, request.voice_volume, request.voice_rate)

        # Stage 5: Subtitles
        tasks[task_id]["progress"] = 75
        subtitles = service.generate_subtitles(audio, script) if request.subtitle_enabled else None

        # Stage 6: Compose
        tasks[task_id]["progress"] = 90
        output = service.compose_video(
            clips=clips,
            audio=audio,
            subtitles=subtitles,
            aspect=request.video_aspect,
            bgm_type=request.bgm_type,
            bgm_volume=request.bgm_volume,
            font_name=request.font_name,
            text_fore_color=request.text_fore_color,
            text_background_color=request.text_background_color,
            font_size=request.font_size,
            stroke_color=request.stroke_color,
            stroke_width=request.stroke_width
        )

        tasks[task_id]["status"] = "completed"
        tasks[task_id]["progress"] = 100
        tasks[task_id]["result"] = {
            "video_path": str(output),
            "script": script,
            "terms": terms,
            "duration": "~30s"
        }

    except Exception as e:
        tasks[task_id]["status"] = "failed"
        tasks[task_id]["error"] = str(e)

    tasks[task_id]["updated_at"] = datetime.now().isoformat()

# ==================== MAIN ====================
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
