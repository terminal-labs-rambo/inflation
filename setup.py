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
from pathlib import Path
from os.path import join, basename, abspath, isdir, isfile, dirname
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

def create_dirs(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

def dl_bash_repos(repos, _tmp):
    for repo in repos:
        urllib.request.urlretrieve(repo["url"], repo["filename"])
        with zipfile.ZipFile(repo["filename"], "r") as zip_ref:
            zip_ref.extractall(_tmp)

def compile_python(name, file, _src):
    with open(os.path.dirname(__file__) + "/" + _src + "/" + name + "/" + file) as f:
        code = compile(f.read(), file, "exec")
        return code

_path = str(pathlib.Path(__file__).parent.absolute())
_src = "src"
_config = "/setup.cfg"
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

exec(compile_python(name + "/" + "framework", "loader.py", _src))
exec(compile_python(name, "local.py", _src))

#f = open(".tmp/logs/setup", "a")
#f.close()

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
