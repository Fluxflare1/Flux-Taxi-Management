# flux_taxi/settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your_sentry_dsn",
    integrations=[DjangoIntegration()],
)
# flux_taxi/settings.py
SECURE_SSL_REDIRECT = True
# flux_taxi/settings.py
INSTALLED_APPS = [
    ...,
    'django_otp',
]
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
