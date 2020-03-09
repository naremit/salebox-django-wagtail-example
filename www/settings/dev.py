from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=s$_=xl+&7+ogd86f81bg$y*v8mwmyt#%$=u$anx!)vim*r$sx'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

INTERNAL_IPS = ['127.0.0.1',]

SALEBOX['API'] = {
    'IP': '<SALEBOX_SERVER_IP>',
    'URL': '<SALEBOX_SERVER_URL>',
    'KEY': '<POS_ID>',
    'LICENSE': '<LICENSE_KEY>',
}
SALEBOX['MISC']['POS_USER_ID'] = 0

try:
    from .local import *
    SALEBOX = local_config(SALEBOX)
except ImportError:
    pass
