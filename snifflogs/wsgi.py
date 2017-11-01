"""
WSGI config for snifflogs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snifflogs.settings")

import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
except Exception:
    print('handling WSGI exception')
    # Error loading applications
    traceback.print_exc()
    os.kill(os.getpid(), signal.SIGINT)
    time.sleep(2.5)
