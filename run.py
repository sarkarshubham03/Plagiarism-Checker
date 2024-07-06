#!/usr/bin/env python
#copy this to execute the code
#C:/Users/"      write your user   "/AppData/Local/Programs/Python/Python312/python.exe4
# D:\Plagiarsim-Checker-main>    &    C:/Users/prave/AppData/Local/Programs/Python/Python312/python.exe    d:/Plagiarsim-Checker-main/run.py   runserver



import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Plagiarism_Checker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
