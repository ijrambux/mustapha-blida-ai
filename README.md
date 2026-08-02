================================================================================
                        MUSTAPHA BLIDA AI
                     AI-Powered Short Video Generator
================================================================================

Developer: https://x.com/mouse0000000
Version: 1.0.0
License: MIT

================================================================================
ABOUT
================================================================================

Mustapha Blida AI is an all-in-one tool for creating high-quality short videos 
using artificial intelligence.

Simply enter a TOPIC or KEYWORD, and the system will automatically:

  - Write a professional video script
  - Search for free stock video footage
  - Generate voiceover narration
  - Add synchronized subtitles
  - Mix background music
  - Export the final video

================================================================================
FEATURES
================================================================================

  AI Powered        - Supports OpenAI, Gemini, DeepSeek, Ollama
  Free Footage      - Searches Pexels & Pixabay
  Voiceover         - Microsoft Edge TTS completely FREE
  Subtitles         - Arabic & English support
  Multiple Ratios   - 9:16 (TikTok), 16:9 (YouTube), 1:1 (Instagram)
  Web UI            - Easy-to-use browser interface
  Full API          - REST API for integration

================================================================================
REQUIREMENTS
================================================================================

  Component     Minimum          Recommended
  ---------     -------          -----------
  CPU           4 cores          6-8 cores
  RAM           4 GB             8-16 GB
  Python        3.11             3.11
  Storage       6 GB free        10+ GB
  FFmpeg        Required         Required

================================================================================
INSTALLATION
================================================================================

Step 1: Install Python Dependencies
------------------------------------
    pip install streamlit openai edge-tts moviepy requests Pillow

Step 2: Install FFmpeg
-----------------------
    Ubuntu/Debian:
        sudo apt update && sudo apt install ffmpeg
    
    macOS:
        brew install ffmpeg
    
    Windows:
        Download from ffmpeg.org and add to PATH

Step 3: Clone the Project
--------------------------
    git clone https://github.com/YOUR_USERNAME/mustapha-blida-ai.git
    cd mustapha-blida-ai

Step 4: Configure API Keys
---------------------------
    cp config.example.toml config.toml

Edit config.toml with your keys:

    [llm]
    openai_api_key = "sk-your-openai-key"
    gemini_api_key = "your-gemini-key"

    [pexels]
    pexels_api_keys = ["your-pexels-key"]

    [pixabay]
    pixabay_api_keys = ["your-pixabay-key"]

================================================================================
USAGE
================================================================================

Web Interface (Streamlit)
--------------------------
    streamlit run webui/Main.py
    
    Open browser at: http://localhost:8501

API Mode
---------
    python main.py
    
    API Docs: http://localhost:8080/docs

Command Line
-------------
    python mustapha_blida_ai_complete.py --cli

Docker
-------
    docker-compose up --build
    
    Web UI: http://localhost:8501
    API:    http://localhost:8080

================================================================================
PROJECT STRUCTURE
================================================================================

mustapha-blida-ai/
|-- app/
|   |-- config/
|   |   |-- config.py              Configuration manager
|   |-- services/
|   |   |-- video_service.py       Video generation engine
|-- webui/
|   |-- Main.py                    Streamlit Web Interface
|-- main.py                        FastAPI Server
|-- config.toml                    Config file (DO NOT upload)
|-- config.example.toml            Config template for users
|-- requirements.txt               Python dependencies
|-- Dockerfile
|-- docker-compose.yml
|-- README.txt                     This file

================================================================================
SUPPORTED LANGUAGES
================================================================================

  Language      Code    TTS Voice
  --------      ----    ---------
  Arabic        ar      ar-SA-ZariyahNeural
  English       en      en-US-JennyNeural
  French        fr      fr-FR-DeniseNeural
  Spanish       es      es-ES-ElviraNeural
  German        de      de-DE-KatjaNeural

================================================================================
FREE API KEYS
================================================================================

  Service       Link                              Cost
  -------       ----                              ----
  Pexels        pexels.com/api                    FREE (200 req/hour)
  Pixabay       pixabay.com/api/docs              FREE (100 req/min)
  Gemini        aistudio.google.com               FREE & generous
  Edge TTS      Built-in                          Completely FREE

================================================================================
TROUBLESHOOTING
================================================================================

  Issue                    Solution
  -----                    --------
  Pexels error             Verify your API key is correct
  No audio                 Install FFmpeg: apt install ffmpeg
  LLM error                Check API balance or try local Ollama
  Slow generation          Use GPU or reduce video quality

================================================================================
CONTRIBUTING
================================================================================

Contributions are welcome!

  1. Fork the project
  2. Create a branch: git checkout -b feature/new-feature
  3. Commit changes: git commit -m "Add new feature"
  4. Push: git push origin feature/new-feature
  5. Open a Pull Request

================================================================================
LICENSE
================================================================================

This project is licensed under the MIT License.

Inspired by MoneyPrinterTurbo (github.com/harry0703/MoneyPrinterTurbo) 
with custom improvements.

================================================================================
DEVELOPER
================================================================================

  Mustapha Blida AI
  
  X (Twitter): https://x.com/mouse0000000
  Contact:     x.com/mouse0000000

================================================================================
                         Made with love by Mustapha Blida AI
================================================================================
