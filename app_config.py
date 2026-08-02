"""
Mustapha Blida AI - Configuration Manager
=========================================
"""

import os
import toml
from pathlib import Path
from typing import List, Optional


class Config:
    """Application configuration loaded from config.toml"""

    APP_NAME = "Mustapha Blida AI"
    APP_VERSION = "1.0.0"
    APP_AUTHOR = "https://x.com/mouse0000000"

    def __init__(self, config_path: str = "config.toml"):
        self.config_path = config_path
        self._config = self._load_config()

    def _load_config(self) -> dict:
        """Load TOML configuration file"""
        if not os.path.exists(self.config_path):
            # Return default config if file doesn't exist
            return self._default_config()

        with open(self.config_path, "r", encoding="utf-8") as f:
            return toml.load(f)

    def _default_config(self) -> dict:
        """Default configuration"""
        return {
            "app": {
                "app_name": self.APP_NAME,
                "app_version": self.APP_VERSION,
                "llm_provider": "openai",
                "video_source": "pexels",
                "tts_provider": "edge",
                "output_dir": "./storage/output"
            },
            "llm": {
                "openai_api_key": "",
                "openai_model_name": "gpt-4o-mini",
                "gemini_api_key": "",
                "gemini_model_name": "gemini-1.5-flash",
                "deepseek_api_key": "",
                "deepseek_model_name": "deepseek-chat",
                "ollama_base_url": "http://localhost:11434",
                "ollama_model_name": "llama3",
            },
            "pexels": {"pexels_api_keys": []},
            "pixabay": {"pixabay_api_keys": []},
            "tts": {"edge_tts_voice": "auto"},
            "subtitle": {
                "font_name": "default",
                "font_size": 60,
                "text_fore_color": "#FFFFFF",
                "stroke_color": "#000000",
                "stroke_width": 1.5,
            },
            "video": {
                "video_aspect": "9:16",
                "video_clip_duration": 3,
            },
            "bgm": {"bgm_type": "random", "bgm_volume": 0.2},
        }

    # App settings
    @property
    def app_name(self) -> str:
        return self._config.get("app", {}).get("app_name", self.APP_NAME)

    @property
    def app_version(self) -> str:
        return self._config.get("app", {}).get("app_version", self.APP_VERSION)

    @property
    def app_author(self) -> str:
        return self._config.get("app", {}).get("app_author", self.APP_AUTHOR)

    @property
    def llm_provider(self) -> str:
        return self._config.get("app", {}).get("llm_provider", "openai")

    @property
    def video_source(self) -> str:
        return self._config.get("app", {}).get("video_source", "pexels")

    @property
    def tts_provider(self) -> str:
        return self._config.get("app", {}).get("tts_provider", "edge")

    @property
    def output_dir(self) -> str:
        return self._config.get("app", {}).get("output_dir", "./storage/output")

    # LLM settings
    @property
    def openai_api_key(self) -> str:
        return self._config.get("llm", {}).get("openai_api_key", "")

    @property
    def openai_model_name(self) -> str:
        return self._config.get("llm", {}).get("openai_model_name", "gpt-4o-mini")

    @property
    def openai_base_url(self) -> str:
        return self._config.get("llm", {}).get("openai_base_url", "https://api.openai.com/v1")

    @property
    def gemini_api_key(self) -> str:
        return self._config.get("llm", {}).get("gemini_api_key", "")

    @property
    def gemini_model_name(self) -> str:
        return self._config.get("llm", {}).get("gemini_model_name", "gemini-1.5-flash")

    @property
    def deepseek_api_key(self) -> str:
        return self._config.get("llm", {}).get("deepseek_api_key", "")

    @property
    def deepseek_model_name(self) -> str:
        return self._config.get("llm", {}).get("deepseek_model_name", "deepseek-chat")

    @property
    def ollama_base_url(self) -> str:
        return self._config.get("llm", {}).get("ollama_base_url", "http://localhost:11434")

    @property
    def ollama_model_name(self) -> str:
        return self._config.get("llm", {}).get("ollama_model_name", "llama3")

    # Video source keys
    @property
    def pexels_api_keys(self) -> List[str]:
        return self._config.get("pexels", {}).get("pexels_api_keys", [])

    @property
    def pixabay_api_keys(self) -> List[str]:
        return self._config.get("pixabay", {}).get("pixabay_api_keys", [])

    # TTS settings
    @property
    def edge_tts_voice(self) -> str:
        return self._config.get("tts", {}).get("edge_tts_voice", "auto")

    # Subtitle settings
    @property
    def subtitle_font_name(self) -> str:
        return self._config.get("subtitle", {}).get("font_name", "default")

    @property
    def subtitle_font_size(self) -> int:
        return self._config.get("subtitle", {}).get("font_size", 60)

    @property
    def subtitle_text_fore_color(self) -> str:
        return self._config.get("subtitle", {}).get("text_fore_color", "#FFFFFF")

    @property
    def subtitle_stroke_color(self) -> str:
        return self._config.get("subtitle", {}).get("stroke_color", "#000000")

    @property
    def subtitle_stroke_width(self) -> float:
        return self._config.get("subtitle", {}).get("stroke_width", 1.5)

    # Video settings
    @property
    def video_aspect(self) -> str:
        return self._config.get("video", {}).get("video_aspect", "9:16")

    @property
    def video_clip_duration(self) -> int:
        return self._config.get("video", {}).get("video_clip_duration", 3)

    # BGM settings
    @property
    def bgm_type(self) -> str:
        return self._config.get("bgm", {}).get("bgm_type", "random")

    @property
    def bgm_volume(self) -> float:
        return self._config.get("bgm", {}).get("bgm_volume", 0.2)
