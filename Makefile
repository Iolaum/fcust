.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

# Disable webbrowser popup temporarily due to flatpak errors.
# webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
print(pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr _rpm/*
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

code: ## code quality checks
	black fcust tests
	flake8 fcust tests
	mypy fcust tests
	check-manifest
	yamllint action.yml
	yamllint .github/workflows
	doc8 docs
	# Dockerfile linting https://github.com/hadolint/hadolint
	hadolint Dockerfile

test: ## run tests quickly with the default Python
	make clean
	pytest

coverage: ## check code coverage quickly with the default Python
	coverage run --source fcust -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/fcust.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ fcust
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(MAKE) -C docs man
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	echo "Showing ./dist/ contents:"
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

fedpkg: # build package for Fedora (37)
	# build package locally
	make dist
	# remove all previous artifacts
	rm -rf _rpm/*
	# move new package to rpm folder
	cp dist/fcust-*.tar.gz ./_rpm/
	# add needed spec file
	cp fcust.spec ./_rpm/
	# create rpm packages
	fedpkg --release f37 --path ./_rpm local
	echo "RPM Files Built!"
	# check rpm packages
	fedpkg --release f37 --path ./_rpm lint
