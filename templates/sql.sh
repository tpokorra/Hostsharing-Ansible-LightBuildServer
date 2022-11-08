#!/bin/bash

cd ~/lbs
. .venv/bin/activate
python manage.py dbshell
