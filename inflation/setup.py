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
        "setuptools<=45",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
        "utilities-package_cli-metapackage@git+https://gitlab.com/terminallabs/utilitiespackage/metapackages/utilities-package_cli-metapackage.git@master#egg=utilitiespackageclimetapackage&subdirectory=utilitiespackageclimetapackage",
        "keyloader@git+https://gitlab.com/terminallabs/experimental-tools/python_key-loader.git@master#egg=keyloader&subdirectory=keyloader",
        "apiwrapper@git+https://gitlab.com/terminallabs/experimental-tools/python_api-wrapper.git@master#egg=apiwrapper&subdirectory=apiwrapper",
        "pyOpenSSL",
    ],
    entry_points="""
        [console_scripts]
        inflation=inflation.cli:main
     """,
)
