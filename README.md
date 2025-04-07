# نظام الامتحانات (Examination System)

نظام إدارة الامتحانات عبر الويب مبني باستخدام Flask وSQLite (للتطوير) / PostgreSQL (للإنتاج).

A web-based examination management system built with Flask and SQLite (for development) / PostgreSQL (for production).

## المميزات (Features)

- إدارة المستخدمين (طلاب، معلمين)
- إنشاء وإدارة الاختبارات
- أنواع مختلفة من الأسئلة (اختيار متعدد، صح/خطأ، مقالي)
- تصحيح تلقائي للأسئلة الموضوعية
- عرض النتائج والتقارير
- واجهة مستخدم سهلة الاستخدام
- دعم كامل لمعادلات LaTeX الرياضية (باستخدام MathJax)

- User management (students, teachers)
- Creating and managing exams
- Different types of questions (multiple choice, true/false, essay)
- Automatic grading for objective questions
- Viewing results and reports
- User-friendly interface
- Full support for LaTeX mathematical equations (using MathJax)

## متطلبات النظام (System Requirements)

- Python 3.9 أو أحدث
- pip (مدير حزم Python)

- Python 3.9 or newer
- pip (Python package manager)

## دليل التثبيت والتشغيل (Setup and Running Guide)

### الطريقة السريعة (Quick Setup - Windows)

للمستخدمين على نظام Windows، يمكنكم استخدام ملف التشغيل السريع:

For Windows users, you can use the quick setup file:

1. قم بتنزيل أو استنساخ المشروع إلى جهاز الكمبيوتر الخاص بك.

1. Download or clone the project to your computer.

2. قم بتشغيل ملف `run_exam_system.bat` بالنقر المزدوج عليه.

2. Run the `run_exam_system.bat` file by double-clicking it.

سيقوم هذا الملف تلقائيًا بـ:
- تثبيت جميع المتطلبات
- إعداد قاعدة البيانات (إذا لم تكن موجودة)
- تشغيل التطبيق

This file will automatically:
- Install all dependencies
- Set up the database (if it doesn't exist)
- Run the application

### خطوات الإعداد اليدوي (Manual Setup Steps)

1. قم بتنزيل أو استنساخ المشروع إلى جهاز الكمبيوتر الخاص بك.

1. Download or clone the project to your computer.

2. قم بإنشاء بيئة Python افتراضية:

2. Create a Python virtual environment:
```bash
python -m venv venv
```

3. قم بتفعيل البيئة الافتراضية:

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. قم بتثبيت المتطلبات:

4. Install the requirements:
```bash
pip install -r requirements.txt
```

5. قم بإعداد متغيرات البيئة:

5. Set up environment variables:
- انسخ ملف `.env.example` إلى `.env`
- قم بتعديل القيم في ملف `.env` حسب احتياجاتك

- Copy the `.env.example` file to `.env`
- Edit the values in the `.env` file according to your needs
```bash
copy .env.example .env
```

6. قم بإعداد قاعدة البيانات:

6. Initialize the database:
```bash
python init_db.py
```

7. (اختياري) قم بإنشاء بيانات تجريبية:

7. (Optional) Create sample data:
```bash
python create_sample_data.py
```

### تشغيل التطبيق (Running the Application)

1. قم بتفعيل البيئة الافتراضية إذا لم تكن مفعلة:

1. Activate the virtual environment if it's not already activated:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

2. قم بتشغيل التطبيق:

2. Run the application:
```bash
python app.py
```

3. افتح المتصفح وانتقل إلى:

3. Open a browser and navigate to:
```
http://localhost:5000
```

### تسجيل الدخول (Login)

- يمكنك تسجيل الدخول باستخدام حسابات تم إنشاؤها باستخدام "create_sample_data.py" أو إنشاء حساب جديد.
- حسابات افتراضية (إذا تم تشغيل البيانات التجريبية):
  - معلم: username: teacher@example.com, password: password
  - طالب: username: student@example.com, password: password

- You can login using accounts created by "create_sample_data.py" or create a new account.
- Default accounts (if sample data was run):
  - Teacher: username: teacher@example.com, password: password
  - Student: username: student@example.com, password: password

### استكشاف الأخطاء وإصلاحها (Troubleshooting)

إذا واجهت أي مشاكل في تشغيل التطبيق، جرب الخطوات التالية:

If you encounter any issues running the application, try the following steps:

1. تأكد من تنشيط البيئة الافتراضية الصحيحة.

1. Make sure the correct virtual environment is activated.

2. تأكد من تثبيت جميع المتطلبات:

2. Make sure all requirements are installed:
```bash
pip install -r requirements.txt
```

3. تحقق من وجود ملف قاعدة البيانات. إذا لم يكن موجودًا، قم بتشغيل:

3. Check if the database file exists. If not, run:
```bash
python init_db.py
```

4. إذا كنت بحاجة إلى إعادة تعيين قاعدة البيانات، قم بحذف ملف "exam_system.db" ثم تشغيل:

4. If you need to reset the database, delete the "exam_system.db" file and then run:
```bash
python init_db.py
```

5. إذا كنت تواجه مشاكل في الترحيل، يمكنك استخدام:

5. If you're having migration issues, you can use:
```bash
python migrate_db.py
```

## الأدوار في النظام (System Roles)

1. المعلم:
   - إنشاء وتعديل الاختبارات
   - إضافة الأسئلة
   - عرض نتائج الطلاب

1. Teacher:
   - Create and modify exams
   - Add questions
   - View student results

2. الطالب:
   - عرض الاختبارات المتاحة
   - تقديم الاختبارات
   - عرض النتائج

2. Student:
   - View available exams
   - Take exams
   - View results

## الميزات الخاصة (Special Features)

### دعم LaTeX (LaTeX Support)

يدعم النظام معادلات LaTeX الرياضية باستخدام MathJax. يمكنك استخدام الصيغة التالية:
- للمعادلات المضمنة: \(...\)
- للمعادلات المعروضة: \[...\]

The system supports LaTeX mathematical equations using MathJax. You can use the following format:
- For inline equations: \(...\)
- For display equations: \[...\]

أمثلة (Examples):
- Inline: \(E = mc^2\)
- Display: \[F = G \frac{m_1 m_2}{r^2}\]

## المساهمة (Contributing)

نرحب بمساهماتكم! يرجى إرسال pull request للمساهمة في تطوير النظام.

We welcome your contributions! Please send a pull request to contribute to the development of the system.
