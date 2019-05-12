"""
Django settings for prj project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

ROOT_PATH = os.path.dirname(__file__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 로그인 접근이 제한 상황에서 page not found 대신 login함수가 실행됨.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$#a4a%)pe=!e=dncp2gax%**wv3!fz&(t*hpvg-me=l^yk4i1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'debug_toolbar',
    'django_extensions',
    'main',
    'shop',
    'blog',
    'pizzas',
    'accounts',
]

LOGIN_REDIRECT_URL = "/"

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # 추가 2
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'prj', 'templates')],
        # 'DIRS': [os.path.join(os.path.dirname(__file__),'../templates')],
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

# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__), 'template').replace('\\','/'),
# )

WSGI_APPLICATION = 'prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #데이터베이스 엔진
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #이 프로젝트에서사용할 데이터베이스파일명
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.mysql',
#         'NAME':     'prj_db',                  # DB 이름
#         'USER':     'root',                    # DB 사용자 이름
#         'PASSWORD': 'mysql1229',              # DB 비밀번호
#         'HOST':     '127.0.0.1',               # DB 서버 주소
#         'PORT':     '',                        # DB 포트 (생략하면 MySQL 디폴트 포트 3306 자동 지정)
#         'OPTIONS':  {'charset': 'utf8mb4'},
#     }
# }

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = '/static/'
# 앱 수준에서 사용할 정적 파일을 static 템플릿 태그에서 지정할 때,
# 여기에 지정한 폴더를 올바르게 구성해서 정적 파일을 저장해 놓으면 됨
# {% static "my_app/example.jpg" %}로 템플릿 태그를 쓸 경우
# 'my_app/static/my_app/example.jpg'로 저장하면 됨

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'prj', 'static'),
    # 프로젝트 수준 정적 파일을 'C:/work/prj/static' 폴더에 저장하겠다는 의미
    # 단일 항목이라도 마지막 쉼표를 써야 함!!!
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 배포 단계에서는 'C:/work/static' 폴더에 모든 정적 파일을 복사해 두고서 서빙
MEDIA_URL = '/media/'  # 항상 '/'로 끝나야 함
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
INTERNAL_IPS = ['127.0.0.1']                            # 추가 3