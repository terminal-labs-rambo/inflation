import os
import sys
import pathlib
import configparser
from pathlib import Path
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)
_path = str(pathlib.Path(__file__).parent.absolute())
_src = "src"
_config = "/setup.cfg"

setup_author = ("Terminal Labs",)
setup_author_email = ("solutions@terminallabs.com",)
setup_license = ("see LICENSE file",)
setup_url = "https://github.com/terminal-labs/inflation"
package_link = ".tmp/symlink"

config = configparser.ConfigParser()
config.read(_path + _config)
version = config["metadata"]["version"]
name = config["metadata"]["name"]

repo_name = name
package_name = repo_name.replace("-", "")
setup_stub_name = package_name
setup_full_name = repo_name
setup_description = setup_full_name.replace("-", " ")


def setup_links():
    _link = package_link + "/"
    Path(_path + "/" + _link).mkdir(parents=True, exist_ok=True)
    if not os.path.islink(_path + "/" + _link + package_name):
        os.symlink(os.path.join(_path, _src), _path + "/" + _link + "/" + package_name)


setup_links()

pins = []

reqs = [
    "setuptools",
    "utilities-package-pinion@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package-pinion.git",
    "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
]

setup(
    name=package_name,
    version=version,
    description=setup_description,
    url=setup_url,
    author=setup_author,
    author_email=setup_author_email,
    license=setup_license,
    package_dir={"": package_link},
    packages=find_packages(where=package_link),
    zip_safe=False,
    include_package_data=True,
    install_requires=pins + reqs,
    entry_points="""
        [console_scripts]
    """
    + f"{setup_stub_name}={setup_stub_name}.__main__:main",
)
