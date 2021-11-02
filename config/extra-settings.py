DEBUG = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = ["127.0.0.1", "194.67.91.99", ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'course',
        'USER': 'midnightdb',
        'PASSWORD': 'Q1Fg4P54B',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}