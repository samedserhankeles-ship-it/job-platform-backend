import os
from pathlib import Path

# --- TEMEL AYARLAR ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK ---
# 1. SECRET_KEY: Ortam değişkeni ayarlanmazsa, uygulama ÇÖKMELİDİR. 
# ASLA koda varsayılan bir sır eklemeyin.
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY ortam değişkeni ayarlanmalıdır!")

# 2. DEBUG: Ortam değişkeninden (RENDER/VERCEL) alır, yoksa False olur.
# Üretimde daima False olmalıdır.
DEBUG = os.environ.get("DEBUG") == "True"

# 3. ALLOWED_HOSTS: Üretimde asla ["*"] olmamalıdır.
if DEBUG:
    # Geliştirme ortamı için
    ALLOWED_HOSTS = ["*"] 
else:
    # Üretim ortamı için: Sunucunuzun ve frontend'inizin alan adlarını buraya ekleyin.
    # Örn: allowed_hosts = [".render.com", "api.jobplatform.com", "127.0.0.1"]
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
    # Boş liste olması durumunda hata fırlatılabilir.

# --- UYGULAMALAR ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    
    # Kendi uygulamalarınız
    "core", 
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static için
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# --- VERİTABANI ---
# PostgreSQL veya başka bir veritabanı kullanıyorsanız burayı değiştirin
# Render'da otomatik SQLite kullanıyorsa bu ayar yeterlidir.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- STATİK DOSYALAR ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --- KULLANICI MODELİ ---
AUTH_USER_MODEL = "core.User"

# --- DRF AYARLARI ---
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

# --- CORS (Frontend bağlantısı için) ---
if DEBUG:
    # Geliştirme ortamında her yerden erişime izin ver (localhost vb.)
    CORS_ALLOW_ALL_ORIGINS = True
else:
    # Üretim ortamında sadece izin verilen adreslerden erişime izin ver
    CORS_ALLOW_ALL_ORIGINS = False
    # Ortam değişkeninden gelen (virgülle ayrılmış) adresleri kullan
    CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "").split(",")


# --- DİĞER AYARLAR ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "tr-tr"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True
