import os
import sys
import shutil
import subprocess
import yaml
from zipfile import ZipFile
from configparser import ConfigParser

from inflation.settings import *

from inflation.config_parser import process_spec_file
from rambo.app import up, destroy, ssh, set_init_vars

CONFIGFILE = "inflation.conf"

TMPDIR = ".tmp"
RAMBOTMP = ".rambo-tmp"
INFLATIONTMP = ".inflation-tmp"
FOOTBALL = "."
FOOTBALLRESOURCES = ".inflation-football-resources"
METAFOOTBALL = ".inm-metafootball"
METAFOOTBALLRESOURCES = ".inflation-metafootball-resources"
CLUSTERMASTER = ".inm-clustermaster"
CLUSTERMASTERRESOURCES = ".inm-clustermaster-resources"


def _resolve_payload_path():
    payload_name = "/payload"
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + ".egg-link"
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path + "/" + PROJECT_NAME + payload_name
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path + payload_name
    return possible_payload_path


def _emit_payload():
    payload_target = os.path.join(METAFOOTBALL, CLUSTERMASTER, CLUSTERMASTERRESOURCES)
    if not os.path.exists(payload_target):
        shutil.copytree(_resolve_payload_path(), payload_target)


def _downloader(url, target, filename):
    if not os.path.exists(target):
        with urllib.request.urlopen(url) as response, open(os.path.join(TMPDIR, filename), "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = os.path.join(TMPDIR, filename)
        with ZipFile(zipfile) as zf:
            zf.extractall(path=TMPDIR)
        shutil.move(os.path.abspath(TMPDIR + "/" + filename.replace(".zip","") + "-master"), target)
        os.remove(TMPDIR + "/" + filename)


def _create_dirs(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)


def _copy_specs():
    full_path_to_metafootballresources = os.path.join(METAFOOTBALL, METAFOOTBALLRESOURCES)
    if not os.path.exists(full_path_to_metafootballresources):
        os.makedirs(full_path_to_metafootballresources)

    dirs = [
        "cluster",
        "extras",
        "nodes",
        "keys"
    ]
    for dir in dirs:
        full_path_to_metafootballresources_dir = os.path.join(full_path_to_metafootballresources, dir)
        if not os.path.exists(full_path_to_metafootballresources_dir):
            shutil.copytree(dir, full_path_to_metafootballresources_dir)

    files = [
        "hypertop.txt",
        "anti-hypertop.txt",
    ]
    for file in files:
        full_path_to_metafootballresources_file = os.path.join(full_path_to_metafootballresources, file)
        if not os.path.exists(full_path_to_metafootballresources_file):
            shutil.copy(file, full_path_to_metafootballresources_file)


def in_inflation_project():
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, CONFIGFILE)):
        print("found inflation project ---- success")
        return True
    else:
        print("does not look like you are in an inflation project")
        return False


def read_config():
    config = ConfigParser()
    config.read(CONFIGFILE)
    print(config.get('inflation-master', 'ramboproject'))


def init():
    dirs = [
        TMPDIR,
        INFLATIONTMP,
        FOOTBALLRESOURCES,
    ]
    _create_dirs(dirs)

    _downloader(
        "https://github.com/terminal-labs/vagrantfiles/archive/master.zip",
        os.path.join(FOOTBALLRESOURCES, "vagrantfiles"),
        "vagrantfiles.zip",
    )

    _downloader(
        "https://github.com/terminal-labs/simple-vbox-server/archive/master.zip",
        os.path.join(FOOTBALLRESOURCES, "simple-vbox-server"),
        "simple-vbox-server.zip",
    )

    _downloader(
        "https://github.com/terminal-labs/rambo_inflation-metafootball/archive/master.zip",
        METAFOOTBALL,
        "rambo_inflation-metafootball",
    )

    _downloader(
        "https://github.com/terminal-labs/rambo_inflation-clustermaster/archive/master.zip",
        METAFOOTBALL + "/.inm-clustermaster",
        "rambo_inflation-clustermaster",
    )

    _emit_payload()
    _copy_specs()


def inflate(filepath):
    #process_spec_file(filepath)
    os.chdir(METAFOOTBALL)
    up(provider="virtualbox")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir(METAFOOTBALL)
    destroy()


def inflation_ssh():
    os.chdir(METAFOOTBALL)
    ssh()


def startvboxserver():
    subprocess.Popen(
        ["python", "vbox-server.py"],
        cwd="/home/user/.inflation/simple-vbox-server",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def stopvboxserver():
    p = subprocess.Popen(["lsof", "-t", "-i:5555"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()
    pid = output.decode("utf-8")
    os.system("kill " + pid)
