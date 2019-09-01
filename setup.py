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

setup(
    name='inflation',
    version='0.0.1.dev',
    description='Clusters',
    url='https://github.com/terminal-labs/inflation',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license=license,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'termcolor',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        inflation=inflation.cli:main
     '''
)
