import os
import sys
import shutil
import subprocess
import urllib.request
from zipfile import ZipFile

from inflation.config_parser import process_spec_file
from rambo.app import up, destroy, ssh, set_init_vars

HOME = "/vagrant"
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_NAME = os.path.join(PROJECT_LOCATION, "..", "inflation-master")

def loadkeys():
    print("stub load keys")


def init():
    directory = HOME + "/.inflation"
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + "/.inflation/minion_repos"
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + "/.inflation/build"
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + "/.inflation/bin"
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + "/.inflation/tmp"
    if not os.path.exists(directory):
        os.makedirs(directory)

    target = os.path.abspath(HOME + "/.inflation/vagrantfiles")
    if not os.path.exists(target):  # Do not overwrite existing saltstack dir. Installs don't delete!
        url = "https://github.com/terminal-labs/vagrantfiles/archive/master.zip"
        filename = "vagrantfiles.zip"
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath("vagrantfiles-master"), target)
        os.remove(filename)

    target = os.path.abspath(HOME + "/.inflation/simple-vbox-server")
    if not os.path.exists(target):  # Do not overwrite existing saltstack dir. Installs don't delete!
        url = "https://github.com/terminal-labs/simple-vbox-server/archive/master.zip"
        filename = "simple-vbox-server.zip"
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath("simple-vbox-server-master"), target)
        os.remove(filename)

    target = os.path.abspath(HOME + "/inflation-master")
    if not os.path.exists(target):  # Do not overwrite existing dir. Installs don't delete!
        url = "https://github.com/terminal-labs/rambo_inflation-master/archive/master.zip"
        filename = "rambo_inflation-master.zip"
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath("rambo_inflation-master-master"), target)
        os.remove(filename)

    target = os.path.abspath(HOME + "/.inflation/tmp/inflation")
    if not os.path.exists(target):  # Do not overwrite existing dir. Installs don't delete!
        url = "https://github.com/terminal-labs/inflation/archive/master.zip"
        filename = ".inflation/tmp/inflation.zip"
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall(".inflation/tmp/inflation")
        if os.path.exists(".inflation/tmp/inflation_resources"):
            shutil.rmtree(".inflation/tmp/inflation_resources", ignore_errors=True)
        shutil.move(".inflation/tmp/inflation/inflation-master/inflation_resources", ".inflation/tmp/inflation_resources")
        if os.path.exists("inflation-master/inflation_resources"):
            shutil.rmtree("inflation-master/inflation_resources", ignore_errors=True)
        shutil.move(".inflation/tmp/inflation_resources", "inflation-master")
        os.remove(filename)
        shutil.rmtree(".inflation/tmp/inflation", ignore_errors=True)


def inflate(filepath):
    process_spec_file(filepath)

    set_init_vars(cwd="/vagrant/inflation-master")
    up(provider="digitalocean")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    set_init_vars(cwd="/vagrant/inflation-master")
    destroy()


def inflation_ssh():
    set_init_vars(cwd="/vagrant/inflation-master")
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
