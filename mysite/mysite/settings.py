# coding: utf-8
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import PIL
from unipath import Path
import ast
access_conf = ast.literal_eval(','.join(open('pass.conf').readlines()).replace('\n',''))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = access_conf['Secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'disqus',
    'django.contrib.sites',
    'ckeditor',
    'ckeditor_uploader',
    'jquery',
    'rest_framework',
    'snippets.apps.SnippetsConfig',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates/blog')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = { #'default':
    #{
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memoria',
        'USER': 'beast',
        'PASSWORD': access_conf['db_pass'],
        'HOST': '192.168.1.3',
        'PORT': '',
    }


}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

#STATIC_URL = '/static/'

#Disqus
DISQUS_API_KEY = access_conf['Disq_Key']
DISQUS_WEBSITE_SHORTNAME = 'memorialab-info'

#Site id
SITE_ID = 1

#Add static
#STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static')
STATIC_ROOT = '/home/beast/djp/mysite/assets/'
STATIC_URL = '/static/'

#STATIC_ROOT      =  BASE_DIR.child('static')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)

#Media

#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

#Redactor
#REDACTOR_OPTIONS = {'lang': 'ru'}
#REDACTOR_UPLOAD = 'uploads/'

#CKeditor
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = PIL
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'eqneditor',
                'spoiler',
                'codesnippet',
            ]),
    },
}
