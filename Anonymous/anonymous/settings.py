"""
Django settings for anonymous project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


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
    'user',
    'board',
    'storages'
]

AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'anonymous.urls'

# 전역 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # 앱 내의 템플릿 폴더와, 바깥의 폴더를 렌더링
            'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'anonymous.common_context.img_url_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'anonymous.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# MEDIA_ROOT = 'upload'

DEFAULT_FILE_STORAGE="storages.backends.s3boto3.S3Boto3Storage"
import json
env_json = 'env.json'

# json 파일을 python이 읽을 수 있도록 dictionary로 변환해주는 함수
with open(env_json) as f:
    env_json = json.loads(f.read())

# DEFAULT_FILE_STORAGE에 설정한 s3에서 가져와서 사용하는 변수들
AWS_ACCESS_KEY_ID=env_json['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=env_json['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME=env_json['S3_BUCKET_NAME']

# 따로 설정해놓은 url -> 화면에서 img를 출력할 떄 env.json에 설정해둔 url을 가져오기 위해 유지보수 적 측면
S3_ROOT_URL=env_json['S3_ROOT_URL']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_json['SECRET_KEY']


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env_json['DATABASE_NAME'],
        'USER' : env_json['DATABASE_USER_NAME'],
        'PASSWORD' : env_json['DATABASE_PASSWORD'],
        'HOST' : env_json['DATABASE_HOST'],
        'PORT' : '5432'
    }
}