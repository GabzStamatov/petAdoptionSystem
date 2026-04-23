<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3.13
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062
"""Django's command-line utility for administrative tasks."""
import os
import sys

<<<<<<< HEAD
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
=======

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> 43179ae0b1d187050f65b771d77fecad00021062
    main()
