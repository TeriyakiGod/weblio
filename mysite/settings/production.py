from decouple import Csv, config

from .base import *  # noqa: F403, F401
from .base import INSTALLED_APPS

DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())

WAGTAILADMIN_BASE_URL = config("WAGTAILADMIN_BASE_URL", default="https://example.com")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")

INSTALLED_APPS += ["storages"]
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# MinIO Settings
AWS_ACCESS_KEY_ID = config("MINIO_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = config("MINIO_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = config("MINIO_BUCKET_NAME", default="django-media")
AWS_S3_ENDPOINT_URL = config("MINIO_ENDPOINT_URL")
AWS_S3_REGION_NAME = config("MINIO_REGION_NAME", default="eu-east-1")
AWS_S3_USE_SSL = config("MINIO_USE_SSL", default=True, cast=bool)
AWS_S3_FILE_OVERWRITE = config("MINIO_FILE_OVERWRITE", default=False, cast=bool)
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = config("MINIO_VERIFY", default=True, cast=bool)
AWS_QUERYSTRING_AUTH = config("MINIO_QUERYSTRING_AUTH", default=True, cast=bool)
AWS_S3_CUSTOM_DOMAIN = None

# Security settings (uncomment for production)
# SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
# SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
# CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)
# SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
# SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)
