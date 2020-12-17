#!/bin/sh

set -e
set -x

./.venv/bin/python3 app/manage.py runserver 0.0.0.0:8000