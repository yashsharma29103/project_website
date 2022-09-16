#!/bin/bash

# Exit early on errors
set -eu

#Python buffers stdout. To show print() of python
export PYTHONUNBUFFERED=true

#Install Python virtual env
VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
    python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

#install requirements
$VIRTUALENV/bin/pip install -r requirements.txt

#run a python server
$VIRTUALENV/bin/python3 app.py