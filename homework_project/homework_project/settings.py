'''
error while starting djConf

Traceback (most recent call last):
  File "manage.py", line 9, in <module>
    from configurations.management import execute_from_command_line
  File "/home/pi/django/dj_01/dj01_venv/lib/python3.7/site-packages/configurations/management.py", line 3, in <module>
    importer.install(check_options=True)
  File "/home/pi/django/dj_01/dj01_venv/lib/python3.7/site-packages/configurations/importer.py", line 49, in install
    importer = ConfigurationImporter(check_options=check_options)
  File "/home/pi/django/dj_01/dj01_venv/lib/python3.7/site-packages/configurations/importer.py", line 67, in __init__
    self.check_options()
  File "/home/pi/django/dj_01/dj01_venv/lib/python3.7/site-packages/configurations/importer.py", line 87, in check_options
    add_help=False)
TypeError: __init__() takes 1 positional argument but 2 were given


'''
###

'''
see https://django-configurations.readthedocs.io/en/stable/

from configurations import Configuration

class Base(Configuration):
    ... all base config
    
    
class Dev(Base):
    DEBUG = True


class Prod(Base):
    DEBUG = False

'''

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's3++wnriju=f6ta)um=go0jp=tkq@ewp*x3(#2&lmn+bzk^(j#'

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
    
    'debug_toolbar',
    
    'learning.apps.LearningConfig',
    'customauth.apps.CustomauthConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'homework_project.urls'

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

WSGI_APPLICATION = 'homework_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

INTERNAL_IPS = '127.0.0.1'

