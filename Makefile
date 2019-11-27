# Install local changes in the system:
# pip install -e <path>/py_openthesaurus

# Release
#
# Steps:
# * Increase version in `./setup.py`
# * Create git tag
#
# More information:
# https://packaging.python.org/tutorials/packaging-projects/

lint:
	pycodestyle --max-line-length=150 py_openthesaurus/*.py

fix_style:
	autopep8 --in-place --aggressive py_openthesaurus/*.py

build:
	python setup.py sdist bdist_wheel

release: build
	twine upload dist/*

test:
	pip install -r requirements.txt
	python -m unittest

.PHONY: lint fix_style build release