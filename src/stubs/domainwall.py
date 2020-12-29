import os
import sys
import shutil
import subprocess
import yaml
import urllib.request
from zipfile import ZipFile

from collections import OrderedDict

from jinja2 import Environment, BaseLoader
from ruamel import yaml

def loadkeys(verbosity="high"):
    auth = {}

    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "auth")):
        if os.path.exists(os.path.join(cwd, "auth", "secrets.yml")):
            secrets_file = os.path.join(cwd, "auth", "secrets.yml")
            with open(secrets_file, "r") as in_fh:
                secrets_dict = yaml.safe_load(in_fh)
                if isinstance(secrets_dict, dict):
                    auth["secrets"] = secrets_dict

    if os.path.exists(os.path.join(cwd, "auth", "keys")):
        files = os.listdir(os.path.join(cwd, "auth", "keys"))
        files.remove(".DS_Store")
        print(files)

    return auth
