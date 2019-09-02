import sys
from setuptools import setup, find_packages

from inflation.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="inflation",
    version=VERSION,
    description="Clusters",
    url="https://github.com/terminal-labs/inflation",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license=license,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["click", "pyyaml"],
    entry_points="""
        [console_scripts]
        inflation=inflation.cli:main
     """,
)
