"""
Django settings for RankTracker project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0vp!xfnmx#c59%jiks#8%v@vl1qyyn(v_^#s2x9kzw^2-+x%s5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MAPS = ['Hanamoura','LunarColony','Anubis','Volskaya','Dorado','JunkerTown','Rialto','Route66','Gibraltar','BlizzardWorld',
        'Einchenwald','Hollywood','KingsRow','Numbani','Ilios','LijiangTower','Nepal','Oasis','no-screen','PLACEMENT']

HEROS = ['Ana', 'Bastion', 'Doomfist', 'Gengi', 'Mccree', 'Pharah', 'Reaper', 'Soldier76', 'Sombra', 'Tracer', 'Hanzo', 
        'JunkRat', 'Mei', 'Torbjörn', 'Widowmaker', 'Dva', 'Orisa', 'Reinhardt', 'Roadhog', 'Winston', 'Zarya', 'Brigitte', 
        'Lucio', 'Mercy', 'Moira', 'Symmetra', 'Zenyatta','CONNECTION LOSE']

ACCOUNTS = ['Main']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'RankTrackerImpl',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RankTracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'RankTrackerImpl/templates'],
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

WSGI_APPLICATION = 'RankTracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/' 

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'RankTrackerImpl/static'), 
)

# REST framework 
REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',         
        'rest_framework.renderers.BrowsableAPIRenderer'     
    ],     
    
    'DEFAULT_PERMISSION_CLASSES': [         
        'rest_framework.permissions.IsAuthenticated',     
    ],     
    
    'DEFAULT_AUTHENTICATION_CLASSES': [         
        'rest_framework.authentication.BasicAuthentication',     
    ],    
    
    'TEST_REQUEST_DEFAULT_FORMAT': 'json' 
}