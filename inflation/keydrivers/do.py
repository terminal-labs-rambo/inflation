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
