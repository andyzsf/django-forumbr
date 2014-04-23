"""
Django settings for test_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# let's make sure forum is available
sys.path.insert(0, os.path.dirname(BASE_DIR))

SECRET_KEY = '-- DONT MIND ME --'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

# for registration
ACCOUNT_ACTIVATION_DAYS = 7


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'registration',
    'forum',  # ;)
)

ROOT_URLCONF = 'test_project.urls'
WSGI_APPLICATION = 'test_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.forum.sqlite3',
    }
}

# i18n
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

from forum.constants import BBCODE, KB

FORUM_MAX_THREAD_IMAGE_SIZE = 1024 * KB
FORUM_MARKUP = BBCODE

