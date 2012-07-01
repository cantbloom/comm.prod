# Django settings for commerical_production project.
from config import ADMIN_INFO, NAME, USER, PASSWORD, HOST, KEY, SENDGRID
import os
#custom auth by max
AUTH_PROFILE_MODULE = 'commProd.UserProfile'


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ADMIN_INFO

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': NAME,    # Or path to database file if using sqlite3.
        'USER': USER,                      # Not used with sqlite3.
        'PASSWORD': PASSWORD,                  # Not used with sqlite3.
        'HOST': HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'public')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/public/'

ADMIN_MEDIA_PREFIX = '/media/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.contrib.messages.context_processors.messages', 
    'django.contrib.auth.context_processors.auth', 
    'django.core.context_processors.static', 
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'commerical_production.urls'
LOGIN_REDIRECT_URL = "/home"
LOGIN_URL = '/login'
APPEND_SLASH=True
# 1 year in milliseconds so basically forever
SESSION_COOKIE_AGE = 31556926000

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'commerical_production.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'commProd',
)


#email settings from sendgrid.com
EMAIL_HOST = SENDGRID['EMAIL_HOST']
EMAIL_HOST_USER = SENDGRID['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = SENDGRID['EMAIL_HOST_PASSWORD']
EMAIL_PORT = SENDGRID['EMAIL_PORT']
EMAIL_USE_TLS = SENDGRID['EMAIL_USE_TLS']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(ROOT_PATH, 'logs/log.log'),
        },
        # Log to a text file that can be rotated by logrotate
        'errorfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(ROOT_PATH, 'logs/error_log.log'),
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['errorfile'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'simple',
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'commProd.views': {
            'handlers': ['logfile'],
            'level': 'INFO', # Or maybe INFO or DEBUG
            'propagate': False,
            'formatter': 'simple',
        },
    },
}
