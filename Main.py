"""
Mustapha Blida AI - Streamlit Web Interface
============================================
Web UI for AI video generation with Arabic & English support.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.config.config import Config
from app.services.video_service import VideoService

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Mustapha Blida AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    .main {
        font-family: 'Tajawal', 'Segoe UI', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }

    h1, h2, h3 {
        font-family: 'Tajawal', sans-serif !important;
    }

    .stButton>button {
        background: linear-gradient(135deg, #e94560, #ff6b6b);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(233, 69, 96, 0.4);
    }

    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 10px;
        color: white;
    }

    .stSelectbox>div>div {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }

    .stSlider>div>div {
        color: #e94560;
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0,0,0,0.8);
        padding: 10px;
        text-align: center;
        color: #888;
        font-size: 12px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

    .footer a {
        color: #e94560;
        text-decoration: none;
    }

    .info-box {
        background: rgba(233,69,96,0.1);
        border: 1px solid rgba(233,69,96,0.3);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }

    .success-box {
        background: rgba(67,233,123,0.1);
        border: 1px solid rgba(67,233,123,0.3);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="font-size: 42px; margin: 0; background: linear-gradient(90deg, #e94560, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🎬 Mustapha Blida AI
        </h1>
        <p style="color: #a0a0a0; font-size: 16px; margin-top: 8px;">
            مولد فيديوهات قصيرة بالذكاء الاصطناعي | AI Short Video Generator
        </p>
        <p style="font-size: 12px; color: #666;">
            <a href="https://x.com/mouse0000000" target="_blank" style="color: #e94560; text-decoration: none;">
                𝕏 @mouse0000000
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== LANGUAGE SELECTOR ====================
lang = st.sidebar.selectbox(
    "🌍 اللغة | Language",
    ["🇦🇪 العربية", "🇺🇸 English"],
    index=0
)

is_arabic = lang == "🇦🇪 العربية"

# Translations
T = {
    "topic": "موضوع الفيديو" if is_arabic else "Video Topic",
    "topic_help": "اكتب موضوع الفيديو (مثال: كيف يغير الذكاء الاصطناعي حياتنا)" if is_arabic else "Enter video topic (e.g., How AI changes daily life)",
    "script": "السيناريو (اختياري)" if is_arabic else "Script (Optional)",
    "script_help": "اتركه فارغاً ليتم توليده تلقائياً بالذكاء الاصطناعي" if is_arabic else "Leave empty for AI-generated script",
    "language": "لغة الفيديو" if is_arabic else "Video Language",
    "aspect": "نسبة العرض" if is_arabic else "Aspect Ratio",
    "aspect_9_16": "📱 عمودي 9:16 (تيك توك / ريلز)" if is_arabic else "📱 Vertical 9:16 (TikTok/Reels)",
    "aspect_16_9": "🖥️ أفقي 16:9 (يوتيوب)" if is_arabic else "🖥️ Horizontal 16:9 (YouTube)",
    "aspect_1_1": "⬜ مربع 1:1 (انستغرام)" if is_arabic else "⬜ Square 1:1 (Instagram)",
    "clip_duration": "مدة كل مقطع (ثواني)" if is_arabic else "Clip Duration (seconds)",
    "voice": "الصوت" if is_arabic else "Voice",
    "voice_auto": "🤖 تلقائي" if is_arabic else "🤖 Auto-detect",
    "voice_ar": "🇸🇦 عربي - زريعة" if is_arabic else "🇸🇦 Arabic - Zariyah",
    "voice_en": "🇺🇸 إنجليزي - جيني" if is_arabic else "🇺🇸 English - Jenny",
    "voice_fr": "🇫🇷 فرنسي - دينيس" if is_arabic else "🇫🇷 French - Denise",
    "subtitle": "الترجمة" if is_arabic else "Subtitles",
    "subtitle_enable": "✅ تفعيل الترجمة" if is_arabic else "✅ Enable Subtitles",
    "subtitle_position": "موقع الترجمة" if is_arabic else "Subtitle Position",
    "position_bottom": "أسفل" if is_arabic else "Bottom",
    "position_top": "أعلى" if is_arabic else "Top",
    "position_center": "وسط" if is_arabic else "Center",
    "font_size": "حجم الخط" if is_arabic else "Font Size",
    "bgm": "الموسيقى الخلفية" if is_arabic else "Background Music",
    "bgm_enable": "🎵 تفعيل الموسيقى" if is_arabic else "🎵 Enable BGM",
    "bgm_volume": "مستوى الصوت" if is_arabic else "BGM Volume",
    "generate": "🚀 إنشاء الفيديو" if is_arabic else "🚀 Generate Video",
    "advanced": "⚙️ إعدادات متقدمة" if is_arabic else "⚙️ Advanced Settings",
    "result": "✅ النتيجة" if is_arabic else "✅ Result",
    "preview": "معاينة الفيديو" if is_arabic else "Video Preview",
    "download": "⬇️ تحميل الفيديو" if is_arabic else "⬇️ Download Video",
    "footer": "صُنع بـ ❤️ بواسطة Mustapha Blida AI | " if is_arabic else "Made with ❤️ by Mustapha Blida AI | ",
    "footer_x": "𝕏 @mouse0000000" if is_arabic else "𝕏 @mouse0000000",
}

# ==================== SIDEBAR ====================
st.sidebar.markdown(f"""
<div style="text-align: center; padding-bottom: 20px;">
    <h3 style="color: #e94560;">🎬 {Config.APP_NAME}</h3>
    <p style="font-size: 12px; color: #888;">v{Config.APP_VERSION}</p>
</div>
""", unsafe_allow_html=True)

# API Status
st.sidebar.markdown("---")
st.sidebar.subheader("🔌 حالة الخدمات | Service Status")

# Check config
try:
    config = Config()
    has_pexels = bool(config.pexels_api_keys)
    has_pixabay = bool(config.pixabay_api_keys)
    has_llm = bool(config.openai_api_key or config.gemini_api_key)

    if has_pexels or has_pixabay:
        st.sidebar.success("✅ مصدر الفيديو متصل | Video source connected")
    else:
        st.sidebar.warning("⚠️ أضف مفتاح Pexels/Pixabay | Add video API key")

    if has_llm:
        st.sidebar.success("✅ LLM متصل | LLM connected")
    else:
        st.sidebar.warning("⚠️ أضف مفتاح LLM | Add LLM API key")

except Exception as e:
    st.sidebar.error(f"❌ خطأ في الإعدادات | Config error: {e}")

st.sidebar.markdown("---")
st.sidebar.info("""
💡 **نصيحة | Tip:**
استخدم مفتاح Gemini المجاني للبدء!
Use free Gemini key to get started!
""")

# ==================== MAIN FORM ====================
with st.container():
    # Topic Input
    topic = st.text_input(
        f"📌 {T['topic']}",
        placeholder=T['topic_help'],
        help=T['topic_help']
    )

    # Two columns for settings
    col_left, col_right = st.columns(2)

    with col_left:
        # Language
        video_lang = st.selectbox(
            T['language'],
            ["ar", "en", "fr", "es", "de"],
            format_func=lambda x: {
                "ar": "🇸🇦 العربية",
                "en": "🇺🇸 English",
                "fr": "🇫🇷 Français",
                "es": "🇪🇸 Español",
                "de": "🇩🇪 Deutsch"
            }.get(x, x)
        )

        # Aspect Ratio
        aspect = st.selectbox(
            T['aspect'],
            ["9:16", "16:9", "1:1"],
            format_func=lambda x: {
                "9:16": T['aspect_9_16'],
                "16:9": T['aspect_16_9'],
                "1:1": T['aspect_1_1']
            }.get(x, x)
        )

        # Voice
        voice = st.selectbox(
            T['voice'],
            ["auto", "ar-SA-ZariyahNeural", "en-US-JennyNeural", "fr-FR-DeniseNeural"],
            format_func=lambda x: {
                "auto": T['voice_auto'],
                "ar-SA-ZariyahNeural": T['voice_ar'],
                "en-US-JennyNeural": T['voice_en'],
                "fr-FR-DeniseNeural": T['voice_fr']
            }.get(x, x)
        )

    with col_right:
        # Clip Duration
        clip_duration = st.slider(
            T['clip_duration'],
            min_value=1,
            max_value=10,
            value=3
        )

        # Subtitle
        subtitle_enabled = st.checkbox(T['subtitle_enable'], value=True)

        if subtitle_enabled:
            subtitle_position = st.selectbox(
                T['subtitle_position'],
                ["bottom", "top", "center"],
                format_func=lambda x: {
                    "bottom": T['position_bottom'],
                    "top": T['position_top'],
                    "center": T['position_center']
                }.get(x, x)
            )

            font_size = st.slider(T['font_size'], 20, 100, 60)

        # BGM
        bgm_enabled = st.checkbox(T['bgm_enable'], value=True)

        if bgm_enabled:
            bgm_volume = st.slider(T['bgm_volume'], 0.0, 1.0, 0.2)

    # Script (optional)
    with st.expander(T['advanced']):
        custom_script = st.text_area(
            T['script'],
            height=150,
            help=T['script_help']
        )

    # Generate Button
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button(T['generate'], use_container_width=True)

# ==================== GENERATION ====================
if generate_btn:
    if not topic.strip():
        st.error("❌ الرجاء إدخال موضوع الفيديو | Please enter a video topic")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()

        stages = [
            ("📝", "جاري كتابة السيناريو..." if is_arabic else "Writing script...", 0.1),
            ("🔍", "جاري استخراج كلمات البحث..." if is_arabic else "Extracting search terms...", 0.2),
            ("🎥", "جاري تحميل لقطات الفيديو..." if is_arabic else "Downloading footage...", 0.4),
            ("🎙️", "جاري إنشاء التعليق الصوتي..." if is_arabic else "Generating voiceover...", 0.6),
            ("📜", "جاري إنشاء الترجمة..." if is_arabic else "Creating subtitles...", 0.75),
            ("🎬", "جاري تركيب الفيديو النهائي..." if is_arabic else "Composing final video...", 0.9),
        ]

        try:
            config = Config()
            service = VideoService(config)

            # Stage 1: Script
            status_text.markdown(f"<div class='info-box'>{stages[0][0]} {stages[0][1]}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(stages[0][2] * 100))

            if custom_script.strip():
                script = custom_script
            else:
                script = service.generate_script(topic, video_lang)

            # Stage 2: Terms
            status_text.markdown(f"<div class='info-box'>{stages[1][0]} {stages[1][1]}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(stages[1][2] * 100))
            terms = service.extract_terms(script, video_lang)

            # Stage 3: Footage
            status_text.markdown(f"<div class='info-box'>{stages[2][0]} {stages[2][1]}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(stages[2][2] * 100))
            clips = service.fetch_footage(terms, clip_duration)

            # Stage 4: Voiceover
            status_text.markdown(f"<div class='info-box'>{stages[3][0]} {stages[3][1]}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(stages[3][2] * 100))
            audio = service.generate_voiceover(script, voice)

            # Stage 5: Subtitles
            if subtitle_enabled:
                status_text.markdown(f"<div class='info-box'>{stages[4][0]} {stages[4][1]}</div>", unsafe_allow_html=True)
                progress_bar.progress(int(stages[4][2] * 100))
                subtitles = service.generate_subtitles(audio, script)
            else:
                subtitles = None

            # Stage 6: Compose
            status_text.markdown(f"<div class='info-box'>{stages[5][0]} {stages[5][1]}</div>", unsafe_allow_html=True)
            progress_bar.progress(int(stages[5][2] * 100))

            output = service.compose_video(
                clips=clips,
                audio=audio,
                subtitles=subtitles,
                aspect=aspect,
                bgm_type="random" if bgm_enabled else "none",
                bgm_volume=bgm_volume if bgm_enabled else 0,
                font_size=font_size if subtitle_enabled else 60,
            )

            # Complete
            progress_bar.progress(100)
            status_text.markdown(f"""
            <div class='success-box'>
                ✅ {"تم إنشاء الفيديو بنجاح!" if is_arabic else "Video created successfully!"}<br>
                📄 <b>{"السيناريو:" if is_arabic else "Script:"}</b><br>
                <pre style='background: rgba(0,0,0,0.3); padding: 10px; border-radius: 5px;'>{script}</pre>
            </div>
            """, unsafe_allow_html=True)

            # Show result
            st.markdown(f"### {T['result']}")
            st.markdown(f"**🎬 {'مسار الفيديو:' if is_arabic else 'Video Path:'}** `{output}`")

            # Note about full implementation
            st.info("""
            💡 **ملاحظة | Note:**
            هذا الإصدار التجريبي يوضح هيكل المشروع. للحصول على الوظائف الكاملة (تحميل الفيديوهات الفعلية، TTS حقيقي، تركيب MoviePy)، استخدم المشروع الكامل من GitHub.

            This is a demo showing the project structure. For full functionality (actual video downloads, real TTS, MoviePy composition), use the complete project from GitHub.
            """)

        except Exception as e:
            st.error(f"❌ {'خطأ:' if is_arabic else 'Error:'} {str(e)}")
            progress_bar.empty()

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    """ + T['footer'] + """<a href="https://x.com/mouse0000000" target="_blank">""" + T['footer_x'] + """</a>
</div>
""", unsafe_allow_html=True)
