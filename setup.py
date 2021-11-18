import os
import sys
import shutil
import pathlib
import zipfile
import configparser
import shlex
import json
import subprocess
import urllib.request
import importlib.util
from pathlib import Path
from os.path import join, basename, abspath, isdir, isfile, dirname
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def create_dirs(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

def dl_bash_repos(repos, _tmp):
    for repo in repos:
        urllib.request.urlretrieve(repo["url"], repo["filename"])
        with zipfile.ZipFile(repo["filename"], "r") as zip_ref:
            zip_ref.extractall(_tmp)

def import_file_as_module(module_name, name, filepath, _src):
    spec = importlib.util.spec_from_file_location(module_name, os.path.dirname(__file__) + "/" + _src + "/" + name + "/" + filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_path = str(pathlib.Path(__file__).parent.absolute())
_src = "src"
_config = "/" + find("setup.cfg", _src)
_tmp = ".tmp"

config = configparser.ConfigParser()
config.read(_path + _config)
version = config["metadata"]["version"]
name = config["metadata"]["name"]

repo_name = name
package_name = repo_name.replace("-", "")
setup_stub_name = package_name
setup_full_name = repo_name
setup_description = setup_full_name.replace("-", " ")

dirs = [".tmp", ".tmp/download", ".tmp/logs"]
create_dirs(dirs)

repos = [
    {
    "url":"https://github.com/terminal-labs/bash-environment-shelf/archive/refs/heads/master.zip",
    "filename":".tmp/download/bash-environment-shelf.zip"
    }
]
dl_bash_repos(repos, _tmp)

_path_to_framework = _src + "/" + name + "/" + "framework"
if os.path.exists(_path_to_framework):
    shutil.rmtree(_path_to_framework)

if not os.path.exists(_path_to_framework):
    shutil.copytree(".tmp/bash-environment-shelf-master/codepacks/framework", _path_to_framework)



_fw_lib = import_file_as_module('lib_fw', name + "/" + "framework", "lib.py", _src)
_local = import_file_as_module('bem_local', name, "local.py", _src)

# f = open(".tmp/logs/setup", "a")
# f.write(find("setup.cfg", "src"))
# f.close()

setup(
    name=package_name,
    version=version,
    description=setup_description,
    url=_local.setup_url,
    author=_local.setup_author,
    author_email=_local.setup_author_email,
    license=_local.setup_license,
    package_dir={"": _local.package_link},
    packages=find_packages(where=_local.package_link),
    zip_safe=False,
    include_package_data=True,
    install_requires=_local.pins + _local.reqs + _fw_lib.smart_reqs(_local.extras, package_name),
    entry_points="""
        [console_scripts]
    """
    + f"{setup_stub_name}={setup_stub_name}.__main__:main",
)
