import os
from vsesrisovki.settings.loggers import *
from vsesrisovki.settings.data import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

AUTH_USER_MODEL = 'users.User'

# Path
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_src'), ]
# Email
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'xxx'
DEFAULT_FROM_EMAIL = 'xxx'
EMAIL_HOST_PASSWORD = 'xxx'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
POST_ADDRESS = 'xxx'
ADMINS = (
    ('WStanley', 'xxx'),
    ('Alex', 'xxx'),
    ('all', POST_ADDRESS),
)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',

    'solo',
    'mptt',
    'ckeditor',
    'imagekit',
    # 'debug_toolbar',
    'rest_framework',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.vk',

    'api',
    'users',
    'front',
    'posts',
    'configs',
    'comments',
    'step_drawing',
]

ROOT_URLCONF = 'vsesrisovki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'django.templatetags.cache',
                'django.templatetags.i18n',
                'django.templatetags.l10n',
                'django.templatetags.tz',
                'django.templatetags.static',
                'front.templatetags.matem',
                'front.templatetags.date_tags',
                'front.templatetags.text'
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.all_template_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'vsesrisovki.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Irkutsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True

X_FRAME_OPTIONS = 'ALLOW-FROM https://mc.yandex.ru/'

# Allauth
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_FORMS = {
    'login': 'utils.allauth_forms.CustomLoginForm',
    'signup': 'utils.allauth_forms.CustomSignupForm',
    'reset_password': 'utils.allauth_forms.CustomResetPasswordForm',
    'reset_password_from_key': 'utils.allauth_forms.CustomResetPasswordKeyForm',
    # 'change_password': 'utils.allauth_forms.CustomChangePasswordForm',
}