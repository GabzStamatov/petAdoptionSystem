"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062

application = get_asgi_application()
