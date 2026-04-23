"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062

application = get_wsgi_application()
