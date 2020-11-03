import os
import django
from django.conf import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings.configure()

settings.INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    # Third part apps
    'django_admin_inline_paginator',
    'tests'
]

settings.TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
    },
]

settings.STATIC_URL = '/'
django.setup()
