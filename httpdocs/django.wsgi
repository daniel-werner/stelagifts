import os
import sys

#path = '/home/vernerd/Django-1.2.4'

#if path not in sys.path:
#    sys.path.insert(0,path)

path = os.path.dirname(__file__) + '/../src'
if path not in sys.path:
    sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 
 
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
