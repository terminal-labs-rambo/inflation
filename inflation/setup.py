import sys
from setuptools import setup, find_packages

from inflation.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="inflation",
    version=VERSION,
    description="Experimental tool for cluster creation and management",
    url="https://github.com/terminal-labs/inflation",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="see LICENSE file",
    packages=["inflation"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
        "ruamel.yaml",
        "rambo-vagrant",
    ],
    entry_points="""
        [console_scripts]
        inflation=inflation.cli:main
     """,
)
