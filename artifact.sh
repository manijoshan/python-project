#! /bin/bash

python3 -m venv venv
. ./venv/bin/activate
          
pip install setuptools
python setup.py sdist 
