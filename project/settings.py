"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
#from django.conf.global_settings import EMAIL_HOST, EMAIL_HOST_USER,\
#    EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS, STATICFILES_DIRS,\
#    LOGIN_REDIRECT_URL
#from test_app.settings import SITE_ID

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='$@m5a#h1oh-=fn4k#!!7tln^u^=km-puzov=f1fpuf(f2x^20p')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = [
    'myiot.pythonanywhere.com',
    '127.0.0.1',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yonestor87@gmail.com'
EMAIL_HOST_PASSWORD = 'electronicaaf0'

"""
Para usar gmail hay que desbloquear el captcha
https://accounts.google.com/displayunlockcaptcha
"""


# Application definition

INSTALLED_APPS = [
    #apps django
    #'registration', #should be immediately above 'django.contrib.admin'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps terceros
    'crispy_forms',
    #'bootstrap4',
    #'widget_tweaks',
    #mis apps
    'estructura',
    'dispositivo',
    'persona',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',        
        
        'NAME': 'data',
        'USER': 'root',
        'PASSWORD': '1223',
        'HOST': '127.0.0.1',
        
        #'NAME': 'lucatronic$gestion',
        #'USER': 'lucatronic',
        #'PASSWORD': 'mysql1234',
        #'HOST': 'lucatronic.mysql.pythonanywhere-services.com',
        
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#/static/imagenes/img1.jpg
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_pro", "static"),
    # '/var/www/static/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "static_root")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_env", "media_root")

CRISPY_TEMPLATE_PACK = 'bootstrap4'
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/tablero/detalle/4'

# Activamos 'CookieStorage' que nos permite enviar los mensajes de respuesta al Crear, Eliminar y Actualizar un registro
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

AUTH_USER_MODEL = "persona.User"

if config('DJANGO_PRODUCTION', default=False, cast=bool):
    from .settings_production import *
