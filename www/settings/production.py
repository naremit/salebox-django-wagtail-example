from .base import *

DEBUG = False

SALEBOX['API'] = {
    'IP': '<SALEBOX_SERVER_IP>',
    'URL': '<SALEBOX_SERVER_URL>',
    'KEY': '<POS_ID>',
    'LICENSE': '<LICENSE_KEY>',
}
SALEBOX['MISC']['POS_USER_ID'] = 0

try:
    from .local import *
except ImportError:
    pass