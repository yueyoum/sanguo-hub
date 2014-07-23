"""
Django settings for gate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FIXTURES_PATH = os.path.join(BASE_DIR, 'fixtures')
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hdbtt87cejsk63ah-g+jab=c^iz@ukhmoib^yn*k+a5zal9q5p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ENABLE_ADMIN = False

ALLOWED_HOSTS = '*'


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'apps.server',
    'apps.account',
    'apps.character',

    'apps.package',
    'apps.mail',
    'apps.purchase',
    'apps.store',
    'apps.activatecode',
    'apps.checkin',
    'apps.production',
    'apps.broadcast',
    'helpers',
)

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'libs.middleware.RequestFilter',
)


ROOT_URLCONF = 'hub.urls'

WSGI_APPLICATION = 'hub.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = False

USE_TZ = True
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# project settings
import xml.etree.ElementTree as et
tree = et.ElementTree(file=os.path.join(BASE_DIR, "config.xml"))

MYSQL_HOST = tree.find('mysql/host').text
MYSQL_PORT = int( tree.find('mysql/port').text )
MYSQL_DB = tree.find('mysql/db').text
MYSQL_USER = tree.find('mysql/user').text
MYSQL_PASSWORD = tree.find('mysql/password').text
MYSQL_AGE = int( tree.find('mysql/age').text )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DB, # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': MYSQL_HOST, # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': MYSQL_PORT, # Set to empty string for default.
        'CONN_MAX_AGE': MYSQL_AGE,
    }
}

CRYPTO_KEY = tree.find('crypto/key').text

MAILGUN_ACCESS_KEY = tree.find('mailgun/key').text
MAILGUN_SERVER_NAME = tree.find('mailgun/domain').text

_CONFIG_ADMINS = tree.find('admins')
ADMINS = ()
for _admin in _CONFIG_ADMINS.getchildren():
    attrib = _admin.attrib
    ADMINS += ((attrib['name'], attrib['email']),)

MANAGERS = ADMINS


THIRD_PLATFORM = {}
_THIRDS = tree.findall('third')
for _TH in _THIRDS:
    _third_data = {}
    for _th in _TH.getchildren():
        _third_data[_th.tag] = _th.text
    THIRD_PLATFORM[_TH.attrib['platform']] = _third_data

del _THIRDS
del _CONFIG_ADMINS
del et
del tree

SERVER_EMAIL = 'hub <hub@sanguo.com>'
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
