#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from pathlib import PurePath

# Needs pip>=20
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

# adapted from:
# https://stackoverflow.com/a/57191701, https://stackoverflow.com/a/59969843
# https://alexanderwaldin.github.io/packaging-python-project.html
requirements0 = parse_requirements(
    str(PurePath.joinpath(PurePath(__file__).parent, "requirements.txt")),
    session=PipSession(),
)
requirements = [str(requirement.requirement) for requirement in requirements0]
del requirements0

dev_requirements = [
    "pip",
    "bump2version>=1.0",
    "wheel",
    "Sphinx",
    "twine",
    "check-manifest",
    "pytest",
    "pytest-runner",
    "mock",
    "flake8",
    "black",
    "mypy",
    "tox",
    "coverage",
    "yamllint",
    "doc8",
    "pluggy<1.0,>=0.12" # Added because of pytest dependency and F32 copr build failure
]

setup(
    author="Nikolaos Perrakis",
    author_email="nikperrakis@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    # Adding man pages to python package: https://stackoverflow.com/a/48381612/1904901
    data_files=[("/usr/share/man/man1/", ["docs/_build/man/fcust.1"])],
    description="Linux Common Folder Custodian",
    entry_points={
        "console_scripts": [
            "fcust=fcust.cli:main",
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fcust",
    name="fcust",
    packages=find_packages(include=["fcust", "fcust.*"]),
    setup_requires=dev_requirements,
    test_suite="tests",
    tests_require=dev_requirements,
    # hack from https://stackoverflow.com/a/41398850/1904901 to be able to install deps from pip
    extras_require={"dev": dev_requirements},
    url="https://github.com/Iolaum/fcust",
    version="0.1.1",
    zip_safe=False,
)
