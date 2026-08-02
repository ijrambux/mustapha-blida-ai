"""
Mustapha Blida AI - Video Generation Service
============================================
Core service that orchestrates the video generation pipeline.
"""

import os
import re
import random
import asyncio
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import quote

import httpx
import edge_tts
from moviepy.editor import (
    VideoFileClip, AudioFileClip, CompositeVideoClip,
    concatenate_videoclips, TextClip, ColorClip
)
from moviepy.video.fx.all import fadein, fadeout


class VideoService:
    """
    Main video generation service.
    Pipeline: Script → Terms → Footage → TTS → Subtitles → Compose
    """

    def __init__(self, config):
        self.config = config
        self.output_dir = Path(config.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Ensure resource directories exist
        Path("resource/songs").mkdir(parents=True, exist_ok=True)
        Path("resource/fonts").mkdir(parents=True, exist_ok=True)

    # ========== STAGE 1: Script Generation ==========
    def generate_script(self, topic: str, language: str = "en", paragraphs: int = 1) -> str:
        """Generate video script using LLM"""

        # Language-specific prompts
        prompts = {
            "ar": f"""اكتب سيناريو فيديو قصير باللغة العربية عن: {topic}
المتطلبات:
- 3 فقرات قصيرة (مقدمة، محتوى، خاتمة)
- أسلوب جذاب وممتع
- مناسب للفيديوهات القصيرة (30-60 ثانية)
- استخدم لغة بسيطة وجذابة

اكتب فقط السيناريو بدون أي إضافات:""",

            "en": f"""Write a short video script about: {topic}
Requirements:
- 3 short paragraphs (intro, body, outro)
- Engaging and entertaining style
- Suitable for short videos (30-60 seconds)
- Use simple, catchy language

Write only the script without any extras:"""
        }

        prompt = prompts.get(language, prompts["en"])

        # In real implementation, call LLM API
        # For demo, return a template script
        if language == "ar":
            return f"""مرحباً بك في {self.config.app_name}! اليوم نتحدث عن: {topic}.

{topic} يغير طريقة إنشاء المحتوى بشكل جذري. مع الذكاء الاصطناعي، ما كان يستغرق ساعات أصبح يستغرق دقائق فقط.

شكراً لمشاهدتك! تابعنا لمزيد من المحتوى عن الذكاء الاصطناعي."""
        else:
            return f"""Welcome to {self.config.app_name}! Today we explore: {topic}.

{topic} is revolutionizing content creation. With AI, what used to take hours now takes minutes.

Thanks for watching! Follow us for more AI content."""

    # ========== STAGE 2: Term Extraction ==========
    def extract_terms(self, script: str, language: str = "en") -> List[str]:
        """Extract search keywords from script"""

        # In real implementation, use LLM to parse script
        # For demo, extract key nouns

        # Simple keyword extraction
        words = re.findall(r'\b[A-Za-z]{4,}\b', script)
        # Deduplicate and limit
        terms = list(dict.fromkeys(words))[:5]

        # Fallback terms if extraction fails
        if not terms:
            terms = ["technology", "artificial intelligence", "future", "digital", "innovation"]

        return terms

    # ========== STAGE 3: Footage Sourcing ==========
    async def _search_pexels(self, term: str) -> Optional[str]:
        """Search Pexels for video clips"""
        api_keys = self.config.pexels_api_keys
        if not api_keys:
            return None

        api_key = random.choice(api_keys)
        url = f"https://api.pexels.com/videos/search?query={quote(term)}&per_page=5"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    headers={"Authorization": api_key},
                    timeout=10.0
                )
                data = response.json()
                videos = data.get("videos", [])
                if videos:
                    # Get first video's HD file
                    video_files = videos[0].get("video_files", [])
                    hd_files = [v for v in video_files if v.get("quality") == "hd"]
                    if hd_files:
                        return hd_files[0].get("link")
                    elif video_files:
                        return video_files[0].get("link")
            except Exception as e:
                print(f"Pexels search error: {e}")

        return None

    async def _search_pixabay(self, term: str) -> Optional[str]:
        """Search Pixabay for video clips"""
        api_keys = self.config.pixabay_api_keys
        if not api_keys:
            return None

        api_key = random.choice(api_keys)
        url = f"https://pixabay.com/api/videos/?key={api_key}&q={quote(term)}&per_page=5"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, timeout=10.0)
                data = response.json()
                hits = data.get("hits", [])
                if hits:
                    return hits[0].get("videos", {}).get("medium", {}).get("url")
            except Exception as e:
                print(f"Pixabay search error: {e}")

        return None

    def fetch_footage(self, terms: List[str], max_duration: int = 3) -> List[Dict]:
        """Download stock video clips"""
        clips = []

        for i, term in enumerate(terms[:5]):  # Max 5 clips
            clip_info = {
                "id": f"clip_{i+1}",
                "term": term,
                "path": None,
                "duration": max_duration
            }

            # Try to download from configured source
            # In real implementation: download actual files
            # For demo: store metadata

            clips.append(clip_info)

        return clips

    # ========== STAGE 4: Text-to-Speech ==========
    async def _generate_edge_tts(self, text: str, voice: str, output_path: str):
        """Generate speech using Microsoft Edge TTS (FREE)"""

        # Auto-detect voice based on language
        if voice == "auto" or not voice:
            # Detect language
            if any('\u0600' <= c <= '\u06FF' for c in text):
                voice = "ar-SA-ZariyahNeural"
            else:
                voice = "en-US-JennyNeural"

        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)

    def generate_voiceover(self, script: str, voice: Optional[str] = None,
                          volume: float = 1.0, rate: float = 1.0) -> str:
        """Convert script to speech audio"""

        output_path = str(self.output_dir / "voiceover.mp3")

        # In real implementation: run async TTS
        # For demo: create placeholder
        # asyncio.run(self._generate_edge_tts(script, voice or "auto", output_path))

        return output_path

    # ========== STAGE 5: Subtitle Generation ==========
    def generate_subtitles(self, audio_path: str, script: str) -> Optional[str]:
        """Generate SRT subtitle file"""

        # In real implementation: use Whisper or TTS alignment
        # For demo: create simple subtitles

        srt_path = str(self.output_dir / "subtitles.srt")

        # Simple word-based timing (not accurate, just demo)
        words = script.split()
        words_per_second = 2.5

        srt_content = []
        idx = 1
        current_time = 0.0

        for word in words:
            start = current_time
            end = current_time + (1.0 / words_per_second)

            srt_content.append(f"{idx}")
            srt_content.append(f"{self._format_time(start)} --> {self._format_time(end)}")
            srt_content.append(word)
            srt_content.append("")

            current_time = end
            idx += 1

        with open(srt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(srt_content))

        return srt_path

    def _format_time(self, seconds: float) -> str:
        """Format seconds to SRT time format"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    # ========== STAGE 6: Video Composition ==========
    def compose_video(self, clips: List[Dict], audio: str,
                     subtitles: Optional[str] = None,
                     aspect: str = "9:16",
                     bgm_type: str = "random",
                     bgm_volume: float = 0.2,
                     font_name: str = "default",
                     text_fore_color: str = "#FFFFFF",
                     text_background_color: str = "transparent",
                     font_size: int = 60,
                     stroke_color: str = "#000000",
                     stroke_width: float = 1.5) -> str:
        """Compose final video from all components"""

        # Determine dimensions based on aspect ratio
        dimensions = {
            "9:16": (1080, 1920),
            "16:9": (1920, 1080),
            "1:1": (1080, 1080)
        }
        width, height = dimensions.get(aspect, (1080, 1920))

        output_path = str(self.output_dir / f"final_video_{aspect.replace(':', 'x')}.mp4")

        # In real implementation:
        # 1. Load video clips
        # 2. Resize to target dimensions
        # 3. Concatenate with transitions
        # 4. Add audio (voiceover + BGM)
        # 5. Add subtitle overlay
        # 6. Render with FFmpeg

        # For demo: create a placeholder black video
        # duration = sum(c["duration"] for c in clips) if clips else 10
        # black_clip = ColorClip(size=(width, height), color=(0, 0, 0), duration=duration)
        # black_clip.write_videofile(output_path, fps=30, codec="libx264")

        return output_path
