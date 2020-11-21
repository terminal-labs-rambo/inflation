import os
import shutil
import urllib
import subprocess
from os.path import isdir, dirname, realpath, abspath, join, exists
from zipfile import ZipFile
from configparser import ConfigParser

from inflation.settings import *


def _delete_dir(directory):
    directory = abspath(directory)
    if exists(directory):
        shutil.rmtree(directory)


def _create_dir(directory):
    directory = abspath(directory)
    if not exists(directory):
        os.makedirs(directory)


def _copy_dir(source, target):
    shutil.copytree(abspath(source), abspath(target))


def _create_dirs(dirs):
    for dir in dirs:
        _create_dir(dir)


def _resolve_payload_path():
    payload_name = "/payload"
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + ".egg-link"
    if exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path + "/" + PROJECT_NAME + payload_name
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path + payload_name
    return possible_payload_path


def _get_github_repo(url, target, filename):
    zipname = filename.replace(".zip", "-master")
    url = url + "/archive/master.zip"
    if not exists(target):
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        # with ZipFile(zipfile) as zf:
        #     zf.extractall()
        # shutil.move(abspath(zipname), target)
        # os.remove(filename)
