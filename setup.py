import sys
from setuptools import setup, find_packages

from inflation.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="inflation",
    version=VERSION,
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="mit",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "standardmodel@git+https://github.com/terminal-labs/standardmodel.git",
        "keyloader@git+https://gitlab.com/terminallabs/experimental-tools/python_key-loader.git@master#egg=keyloader&subdirectory=keyloader",
        "apiwrapper@git+https://gitlab.com/terminallabs/experimental-tools/python_api-wrapper.git@master#egg=apiwrapper&subdirectory=apiwrapper",
    ],
    entry_points="""
        [console_scripts]
        inflation=inflation.cli:main
     """,
)
