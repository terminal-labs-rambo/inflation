import os
import shutil
import urllib
import subprocess
from os.path import isdir, dirname, realpath, abspath, join, exists
from zipfile import ZipFile
from configparser import ConfigParser

from inflation.settings import *

def _get_github_repo(url, target, filename, extract):
    zipname = filename.replace(".zip", "-master")
    url = url + "/archive/master.zip"
    if not exists(target):
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall(path=extract)
