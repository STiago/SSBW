"""
Django settings for my_website project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import mongoengine
from pymongo import read_preferences

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a7l+y+=v96gzno5j_s-5b+pxpiv2)pxtj5ih%@^_hj)5(s)9kw'

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
    'recipes_dashboard',

    #'django_mongoengine',
    #'bootstrap4',
]

#AUTH_USER_MODEL = 'mongo_auth.MongoUser'

#AUTHENTICATION_BACKENDS = (
#    'django_mongoengine.mongo_auth.backends.MongoEngineBackend',
#)

#SESSION_ENGINE = 'django_mongoengine.sessions'


#INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'my_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        #'ENGINE': 'django_mongodb_engine',
        #'NAME': 'mongodb',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
        #'USER': 'devadmin',
        #'PASSWORD': 'password',
        #'HOST': 'localhost',
        #'PORT': '27017',
        #'SUPPORTS_TRANSACTIONS': False,
    }
}
#SESSION_ENGINE = 'mongoengine.django.sessions'

#_MONGODB_USER = 'devadmin'#mongouser
#_MONGODB_PASSWD = 'password'
#_MONGODB_HOST = 'localhost:27017'
#_MONGODB_NAME = 'mongodb'
#_MONGODB_DATABASE_HOST = \
#    'mongodb://%s:%s@%s/%s' \
#    % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

#mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

#AUTHENTICATION_BACKENDS = (
#    'mongoengine.django.auth.MongoEngineBackend',
#)

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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
