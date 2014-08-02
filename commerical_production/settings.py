# Django settings for commerical_production project.
from os import environ as env
import os

# custom auth
AUTH_PROFILE_MODULE = 'commProd.UserProfile'

BASE_URL_PROD = 'http://www.burtonthird.com'
BASE_URL_DEV = 'http://www.burtonthird.com'

DEBUG = (not env['DEBUG'] == 'False')  # convert from sting to bool
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Joshua Blum', 'joshblum@mit.edu'),
    ('Max Kanter', 'kanter@mit.edu'),
    ('comm.prod-admins', 'comm.prod@mit.edu'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if using sqlite3.
        'NAME': env['MYSQL_NAME'],
        'USER': env['MYSQL_USER'],  # Not used with sqlite3.
        'PASSWORD': env['MYSQL_PASSWORD'],  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': env['MYSQL_HOST'],
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

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
MEDIA_ROOT = os.path.join(SITE_ROOT, 'public')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/public/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

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
    'compressor.finders.CompressorFinder',
)

# settings for django-compressor
# COMPRESS_ENABLED = True ##todo move to static files
COMPRESS_CSS_FILTERS = (
    'compressor.filters.template.TemplateFilter',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env['SECRET_KEY']

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
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'helpers.profiler.ProfileMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'commerical_production.backends.EmailOrUsernameBackend',
    'django.contrib.auth.backends.ModelBackend'
)

ROOT_URLCONF = 'commerical_production.urls'
LOGIN_REDIRECT_URL = "/home"
LOGIN_URL = '/login'

# a week in milliseconds
SESSION_COOKIE_AGE = 1000 * 60 * 60 * 24 * 7  # so basically forever

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'commerical_production.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_admin_bootstrapped',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    # third party
    'compressor',
    'django_evolution',
    'pagination',
    'gunicorn',

    # comm.prod
    'migrations',
    'donations',
    'common',
    'commProd',
    'helpers',
    'cron',
)


# email settings from sendgrid.com
EMAIL_HOST = env['EMAIL_HOST']
EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['PASSWORD']
EMAIL_PORT = env['EMAIL_PORT']
EMAIL_USE_TLS = env['EMAIL_USE_TLS']

# gravatar settings
GRAVATAR_IMG_CLASS = "author-pic"
DEFAULT_IMG = "/public/img/placeholder.jpg"

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
            'filename': os.path.join(SITE_ROOT, 'logs/log.log'),
        },
        # Log to a text file that can be rotated by logrotate
        'errorfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(SITE_ROOT, 'logs/error_log.log'),
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
        'commProd.views': {
            'handlers': ['logfile'],
            'level': 'INFO',  # Or maybe INFO or DEBUG
            'propagate': False,
            'formatter': 'simple',
        },
    },
}

if DEBUG:
    # allowing for local_settings overides
    # how this should ultimately be set up
    # is that common or default settings go in here,
    # and each different deploy location has a differnt
    # settings override that is specified by environment
    # variable or hard code.

    try:
        local_settings_file = open("%s/%s" % (SITE_ROOT, "local_settings.py"))
        local_settings_script = local_settings_file.read()
        exec local_settings_script
    except IOError, e:
        print "Unable to open local settings! %s" % e
