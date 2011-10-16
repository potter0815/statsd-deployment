"""
WSGI application configuration.

Read http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango to learn
more about integrating with Django.
"""

import os
import site
import sys

#
# Settings configuration
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'graphite.settings'


#
# Path information
#
PATHS = [
    "/home/web/lib/python2.6/site-packages"
]


#
# Virtualenv configuration
#
activate_this = "/home/web/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))


#
# Path Configuration
# Configure the system path for the wsgi process to mirror the virtualenv
# http://code.google.com/p/modwsgi/wiki/VirtualEnvironments
#

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for path in PATHS:
  site.addsitedir(path)

# Reorder sys.path so new directories are at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path


#
# Define the wsgi application
#

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
