#!/usr/bin/env python
import os
import sys
from bottle import run


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobottle.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    #run(host='localhost', port=8080, debug=True, reloader=True)
