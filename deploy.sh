#!/bin/sh

# register
# python setup.py register
# https://pypi.python.org/pypi?%3Aaction=submit_form

python setup.py check -r -s
python setup.py sdist bdist_wheel

twine upload dist/*
