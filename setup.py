# Before anything else, bail if not Python3
import sys
if sys.version_info.major < 3:
    sys.exit('Python 3 required but lower version found. Aborted.')

import json
import os
import shutil
import urllib.request
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist
from setuptools.command.egg_info import egg_info
from setuptools.command.develop import develop
from setuptools.command.install import install
from zipfile import ZipFile

from inflation.settings import *

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description='Clusters',
    url='https://github.com/terminal-labs/inflation',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license=license,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyyaml',
        'click',
        'termcolor'
    ],
    classifiers = [
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
    ],
    entry_points='''
        [console_scripts]
        inflation=inflation.cli:main
     '''
)
