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


def keydriver_digitalocean():
    pass


def keydriver_aws():
    pass


def replace_in_file(filepath, old, new):
    f = open(filepath, "r")
    contents = f.read()
    f.close()
    contents = contents.replace("-APITOKEN-","aaaaaaaaaaaa")
    contents = contents.replace("-DIGITALOCEANPRIVATEKEYPATH-","bbbbbbbbbbbb")
    f = open(filepath, "w")
    f.write(contents)
    f.close()


def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result


def validate_keys_dict():
    return True


def in_project_dir(verbosity="high"):
    def closure_print(data):
        if verbosity == "high":
            print(data)

    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "hypertop.sls")):
        closure_print("found project ---- success")
        return True
    else:
        closure_print("does not look like you are in an project")
        return False


def scankeys(keyspath):
    with open(keyspath, 'r') as stream:
        keysdata = yaml.safe_load(stream)
        assert validate_keys_dict(keysdata)
        return keysdata


def loadkeysdict(keyspath):
    if os.path.exists(keyspath):
        return scankeys(keyspath)


def loadkeys(verbosity="high"):
    def closure_print(data):
        print(data)

    cwd = os.getcwd()
    if in_project_dir():
        if os.path.exists(os.path.join(cwd, "keys")):
            closure_print("found keys dir ------------- success")
            if os.path.exists(os.path.join(cwd, "keys", "keys.yaml")):
                keys_file = os.path.join(cwd, "keys", "keys.yaml")
                with open(keys_file, "r") as in_fh:
                    keys_dict = yaml.safe_load(in_fh)
                    if isinstance(keys_dict, dict):
                        if validate_keys_dict():
                            closure_print("found keys yaml file ------------- success")
                            closure_print(f"found keys for { len(keys_dict.keys()) } providers ------------- success")
                            return keys_dict
        else:
            closure_print("cant find keys dir ------------- failed")
