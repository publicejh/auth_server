import os
import json
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# .config_secret 폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'rest_framework_api_key',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'corsheaders',

    'accounts',
]

# CorsMiddleware should be placed as high as possible, especially before any middleware that can generate responses
# such as Django’s CommonMiddleware or Whitenoise’s WhiteNoiseMiddleware.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auth_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'auth_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


REST_FRAMEWORK = {
    # 'DATETIME_INPUT_FORMATS': '%Y-%m-%dT%H:%M:%S+09:00',
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S+09:00',

    'DEFAULT_PERMISSION_CLASSES': (
        # will deny permission to any unauthenticated user
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

# make localhost available
SITE_ID = 1

# this will avoid the need for an SMTP server as e=mails, will be printed to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_SESSION_LOGIN = False

REST_USE_JWT = True

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
