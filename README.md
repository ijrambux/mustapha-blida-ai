<div align="center">
🎬 Mustapha Blida AI
مولد فيديوهات قصيرة بالذكاء الاصطناعي
AI-Powered Short Video Generator
https://python.org
LICENSE
https://x.com/mouse0000000
</div>
🌟 نبذة عن المشروع | About
Mustapha Blida AI هو أداة متكاملة لإنشاء فيديوهات قصيرة عالية الجودة باستخدام الذكاء الاصطناعي.
ما عليك سوى إدخال موضوع أو كلمة مفتاحية، وسيقوم النظام تلقائياً بـ:
✍️ كتابة سيناريو احترافي
🔍 البحث عن لقطات فيديو مجانية
🎙️ إنشاء تعليق صوتي
📜 إضافة ترجمة متزامنة
🎵 دمج موسيقى خلفية
🎬 تصدير الفيديو النهائي
🚀 المميزات | Features
Table
الميزة	الوصف
🤖 ذكاء اصطناعي	يدعم OpenAI, Gemini, DeepSeek, Ollama
🎥 لقطات مجانية	يبحث في Pexels و Pixabay
🎙️ تعليق صوتي	Microsoft Edge TTS مجاني بالكامل
📜 ترجمة	دعم اللغة العربية والإنجليزية
📐 نسب متعددة	9:16 (تيك توك)، 16:9 (يوتيوب)، 1:1 (انستغرام)
🌐 واجهة ويب	سهلة الاستخدام عبر المتصفح
🔌 API كامل	REST API للتكامل مع مشاريع أخرى
📋 المتطلبات | Requirements
Table
المكون	الحد الأدنى	الموصى به
المعالج	4 أنوية	6–8 أنوية
الذاكرة	4 GB	8–16 GB
بايثون	3.11	3.11
التخزين	6 GB فارغ	10+ GB
FFmpeg	مطلوب	مطلوب
⚙️ التثبيت | Installation
1️⃣ تثبيت المتطلبات
bash
pip install streamlit openai edge-tts moviepy requests Pillow
2️⃣ تثبيت FFmpeg
Ubuntu/Debian:
bash
sudo apt update && sudo apt install ffmpeg
macOS:
bash
brew install ffmpeg
Windows:
حمّل من ffmpeg.org وأضفه إلى PATH
3️⃣ تثبيت المشروع
bash
git clone https://github.com/YOUR_USERNAME/mustapha-blida-ai.git
cd mustapha-blida-ai
4️⃣ الإعدادات
bash
cp config.example.toml config.toml
عدّل ملف config.toml بمفاتيحك:
toml
[llm]
# اختر أحد المزودين:
openai_api_key = "sk-your-openai-key"
gemini_api_key = "your-gemini-key"  # مجاني!

[pexels]
pexels_api_keys = ["your-pexels-key"]  # مجاني من pexels.com/api

[pixabay]
pixabay_api_keys = ["your-pixabay-key"]  # مجاني من pixabay.com/api/docs
🎯 التشغيل | Usage
🌐 واجهة الويب (Streamlit)
bash
streamlit run webui/Main.py
افتح المتصفح على: http://localhost:8501
📡 وضع API
bash
python main.py
API Docs: http://localhost:8080/docs
🖥️ وضع سطر الأوامر
bash
python mustapha_blida_ai_complete.py --cli
🐳 Docker
bash
# بناء وتشغيل
docker-compose up --build

# واجهة الويب: http://localhost:8501
# API: http://localhost:8080
📁 هيكل المشروع | Project Structure
plain
mustapha-blida-ai/
├── app/
│   ├── config/
│   │   └── config.py          # إدارة الإعدادات
│   └── services/
│       └── video_service.py   # محرك توليد الفيديو
├── webui/
│   └── Main.py                # واجهة الويب (Streamlit)
├── main.py                    # FastAPI Server
├── config.toml                # ⚠️ ملف الإعدادات (لا ترفعه)
├── config.example.toml        # نموذج الإعدادات
├── requirements.txt           # المتطلبات
├── Dockerfile
├── docker-compose.yml
└── README.md
🌍 دعم اللغات | Supported Languages
Table
اللغة	الكود	صوت TTS
🇸🇦 العربية	ar	ar-SA-ZariyahNeural
🇺🇸 الإنجليزية	en	en-US-JennyNeural
🇫🇷 الفرنسية	fr	fr-FR-DeniseNeural
🇪🇸 الإسبانية	es	es-ES-ElviraNeural
🇩🇪 الألمانية	de	de-DE-KatjaNeural
🔑 الحصول على مفاتيح API مجانية
Table
الخدمة	الرابط	التكلفة
Pexels	pexels.com/api	مجاني (200 طلب/ساعة)
Pixabay	pixabay.com/api/docs	مجاني (100 طلب/دقيقة)
Gemini	aistudio.google.com	مجاني وسخي
Edge TTS	مدمج في المشروع	مجاني بالكامل
🛠️ حل المشاكل | Troubleshooting
Table
المشكلة	الحل
خطأ في Pexels	تأكد من صحة مفتاح API
لا يوجد صوت	تثبيت FFmpeg: apt install ffmpeg
خطأ في LLM	تحقق من رصيد API أو جرب Ollama المحلي
بطء التوليد	استخدم GPU أو قلل جودة الفيديو
🤝 المساهمة | Contributing
نرحب بمساهماتكم!
Fork المشروع
أنشئ فرع جديد: git checkout -b feature/ميزة-جديدة
ارتكب التغييرات: git commit -m "إضافة ميزة جديدة"
ادفع: git push origin feature/ميزة-جديدة
افتح Pull Request
📜 الترخيص | License
هذا المشروع مرخص بموجب MIT License.
مستوحى من MoneyPrinterTurbo بتحسينات وتعديلات.
👤 المطور | Developer
<div align="center">
Mustapha Blida AI
https://x.com/mouse0000000
📩 للتواصل والاستفسارات: x.com/mouse0000000
</div>
<div align="center">
  <sub>صُنع بـ ❤️ بواسطة Mustapha Blida AI</sub>
</div>
