# استخدم صورة Python الرسمية
FROM python:3.11-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات المشروع إلى داخل الحاوية
COPY . .

# تثبيت Poetry
RUN pip install poetry

# تثبيت التبعيات باستخدام Poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# فتح البورت (فقط إذا تحتاجه – احذفه إن كنت تستخدم Background Worker فقط)
# EXPOSE 8080

# أمر التشغيل
CMD ["python", "main.py"]