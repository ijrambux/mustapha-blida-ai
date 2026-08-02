<div align="center">
🎬 Mustapha Blida AI
مولد فيديوهات قصيرة بالذكاء الاصطناعي
https://github.com/mustaphablida/mustapha-blida-ai
https://python.org
LICENSE
https://x.com/mouse0000000
</div>
🌟 نبذة عن المشروع
Mustapha Blida AI هو أداة متكاملة لإنشاء فيديوهات قصيرة عالية الجودة باستخدام الذكاء الاصطناعي. ما عليك سوى إدخال موضوع أو كلمة مفتاحية، وسيقوم النظام تلقائياً بـ:
✍️ كتابة سيناريو احترافي
🔍 البحث عن لقطات فيديو مجانية
🎙️ إنشاء تعليق صوتي
📜 إضافة ترجمة متزامنة
🎵 دمج موسيقى خلفية
🎬 تصدير الفيديو النهائي
📸 معاينة الواجهة
<div align="center">
  <img src="docs/preview.png" alt="Mustapha Blida AI Preview" width="800"/>
</div>
🚀 المميزات
Table
الميزة	الوصف
🤖 ذكاء اصطناعي	يدعم 13+ مزود LLM (OpenAI, Gemini, DeepSeek, Ollama...)
🎥 لقطات مجانية	يبحث في Pexels و Pixabay
🎙️ تعليق صوتي	Microsoft Edge TTS مجاني بالكامل
📜 ترجمة	دعم اللغة العربية والإنجليزية
📐 نسب متعددة	9:16 (تيك توك)، 16:9 (يوتيوب)، 1:1 (انستغرام)
🌐 واجهة ويب	سهلة الاستخدام عبر المتصفح
🔌 API كامل	REST API للتكامل مع مشاريع أخرى
📋 المتطلبات
Table
المكون	الحد الأدنى	الموصى به
المعالج	4 أنوية	6–8 أنوية
الذاكرة	4 GB	8–16 GB
بايثون	3.11	3.11
التخزين	6 GB فارغ	10+ GB
⚙️ التثبيت
الطريقة 1: Docker (الأسهل)
bash
git clone https://github.com/mustaphablida/mustapha-blida-ai.git
cd mustapha-blida-ai
cp config.example.toml config.toml
# عدّل config.toml بمفاتيحك
sudo docker compose -f docker-compose.yml up
🌐 واجهة الويب: http://localhost:8501
📡 API: http://localhost:8080/docs
الطريقة 2: التثبيت اليدوي
bash
# 1. تحميل المشروع
git clone https://github.com/mustaphablida/mustapha-blida-ai.git
cd mustapha-blida-ai

# 2. تثبيت Python 3.11
uv python install 3.11
uv sync --frozen

# 3. تشغيل واجهة الويب
sh webui.sh

# 4. تشغيل API (في طرفية جديدة)
uv run python main.py
🔑 الإعدادات
انسخ الملف وعدّله:
bash
cp config.example.toml config.toml
المفاتيح المطلوبة:
toml
[app]
llm_provider = "openai"      # أو: gemini, deepseek, ollama, openrouter
video_source = "pexels"      # أو: pixabay

# مفتاح OpenAI (اختياري إذا استخدمت Gemini المجاني)
openai_api_key = "sk-your-key"
openai_model_name = "gpt-4o-mini"

# مفتاح Pexels (مجاني من: pexels.com/api)
pexels_api_keys = ["your-pexels-key"]

# مفتاح Pixabay (مجاني من: pixabay.com/api/docs)
pixabay_api_keys = ["your-pixabay-key"]

# التعليق الصوتي (مجاني)
tts_provider = "edge"
🎯 كيفية الاستخدام
عبر الويب (Streamlit)
افتح المتصفح على http://localhost:8501
اكتب موضوع الفيديو (مثال: "كيف يغير الذكاء الاصطناعي حياتنا")
اختر اللغة: العربية أو الإنجليزية
اختر نسبة العرض: 9:16 (للتيك توك)
اضغط إنشاء الفيديو 🚀
انتظر 2–5 دقائق ⏳
حمّل الفيديو النهائي! 🎉
عبر API
bash
curl -X POST "http://localhost:8080/api/v1/videos" \
  -H "Content-Type: application/json" \
  -d '{
    "video_subject": "AI and the Future",
    "video_language": "ar",
    "video_aspect": "9:16"
  }'
📁 هيكل المشروع
plain
mustapha-blida-ai/
├── app/                    # منطق التطبيق الأساسي
│   ├── config/            # الإعدادات
│   ├── models/            # نماذج البيانات
│   ├── services/          # الخدمات (LLM, TTS, Video)
│   └── utils/             # أدوات مساعدة
├── webui/                 # واجهة الويب (Streamlit)
│   ├── Main.py            # الصفحة الرئيسية
│   └── components/        # المكونات
├── main.py                # نقطة دخول API (FastAPI)
├── config.toml            # ملف الإعدادات
├── requirements.txt       # المتطلبات
├── Dockerfile             # Docker
└── README.md              # هذا الملف
🌍 دعم اللغات
يدعم المشروع أكثر من 100 لغة بما فيها:
Table
اللغة	الكود	صوت TTS
🇸🇦 العربية	ar	ar-SA-ZariyahNeural
🇺🇸 الإنجليزية	en	en-US-JennyNeural
🇫🇷 الفرنسية	fr	fr-FR-DeniseNeural
🇪🇸 الإسبانية	es	es-ES-ElviraNeural
🇩🇪 الألمانية	de	de-DE-KatjaNeural
🛠️ حل المشاكل
Table
المشكلة	الحل
خطأ في Pexels	تأكد من صحة مفتاح API
لا يوجد صوت	تثبيت FFmpeg: apt install ffmpeg
خطأ في LLM	تحقق من رصيد API أو جرب Ollama المحلي
بطء التوليد	استخدم GPU أو قلل جودة الفيديو
🤝 المساهمة
نرحب بمساهماتكم! 🙏
Fork المشروع
أنشئ فرع جديد: git checkout -b feature/ميزة-جديدة
ارتكب التغييرات: git commit -m "إضافة ميزة جديدة"
ادفع: git push origin feature/ميزة-جديدة
افتح Pull Request
📜 الترخيص
هذا المشروع مرخص بموجب MIT License.
مستوحى من MoneyPrinterTurbo بتحسينات وتعديلات.
👤 المطور
<div align="center">
Mustapha Blida AI — صناعة فيديوهات بالذكاء الاصطناعي
https://x.com/mouse0000000
📩 للتواصل والاستفسارات: x.com/mouse0000000
</div>
<div align="center">
  <sub>صُنع بـ ❤️ بواسطة Mustapha Blida AI</sub>
</div>
