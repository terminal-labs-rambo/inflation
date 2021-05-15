import os
import sys
import pathlib
import configparser
from pathlib import Path
from os.path import join, basename, abspath, isdir, isfile, dirname
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

with open(os.path.dirname(__file__) + "/local.py") as f:
    code = compile(f.read(), "local.py", "exec")
    exec(code)

_path = str(pathlib.Path(__file__).parent.absolute())
_src = "src"
_config = "/setup.cfg"

config = configparser.ConfigParser()
config.read(_path + _config)
version = config["metadata"]["version"]
name = config["metadata"]["name"]

repo_name = name
package_name = repo_name.replace("-", "")
setup_stub_name = package_name
setup_full_name = repo_name
setup_description = setup_full_name.replace("-", " ")

#setup_links(package_name)

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
    install_requires=pins + reqs + smart_reqs(extras, package_name),
    entry_points="""
        [console_scripts]
    """
    + f"{setup_stub_name}={setup_stub_name}.__main__:main",
)
