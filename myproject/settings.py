import os

# settings.py

# Ensure this is added at the beginning to set BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    # Other apps...
    'products',
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'resin_3d_printing',
        'CLIENT': {
            'host': os.environ.get('MONGO_URI'),  # Ensure MONGO_URI is set in the environment
            'username': os.environ.get('MONGO_USERNAME'),  # Optional
            'password': os.environ.get('MONGO_PASSWORD'),  # Optional
            'authSource': 'admin',  # Usually 'admin'
        }
    }
}

SECRET_KEY = 'your_secret_key'

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".gitpod.io"]