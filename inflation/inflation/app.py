import os
import sys
import shutil
import subprocess
import yaml
import urllib.request
from zipfile import ZipFile

from inflation.config_parser import process_spec_file
from rambo.app import up, destroy, ssh, set_init_vars

HOME = "/vagrant"
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_NAME = os.path.join(PROJECT_LOCATION, "..", "inflation-master")


def in_inflation_project():
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "inflation.conf")):
        print("found inflation project ---- success")
        return True
    else:
        print("does not look like you are in an inflation project")
        return False


def replace_in_file(filepath, old, new):
    f = open(filepath, "r")
    contents = f.read()
    f.close()
    contents = contents.replace("-APITOKEN-","aaaaaaaaaaaa")
    contents = contents.replace("-DIGITALOCEANPRIVATEKEYPATH-","bbbbbbbbbbbb")
    f = open(filepath, "w")
    f.write(contents)
    f.close()


def scankeys():
    with open("keys/keys.yaml", 'r') as stream:
        keysdata = yaml.safe_load(stream)
        print(keysdata)
        return keysdata


def loadkeys():
    cwd = os.getcwd()
    if in_inflation_project():
        if os.path.exists(os.path.join(cwd, "keys")):
            print("found keys dir ------------- success")
            if os.path.exists(os.path.join(cwd, "inflation-master", "auth")):
                shutil.rmtree(os.path.join(cwd, "inflation-master", "auth"), ignore_errors=True)
            print("injecting keys ------------- success")
            if not os.path.exists(os.path.join(cwd, "inflation-master", "auth")):
                os.makedirs(os.path.join(cwd, "inflation-master", "auth"))
                shutil.copytree(os.path.abspath("keys"), os.path.join(cwd, "inflation-master", "auth", "keys"))
                url = "https://raw.githubusercontent.com/terminal-labs/inflation/master/inflation_resources/templates/env.sh.template"
                filename = "auto-generated-env.sh"
                with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
                    shutil.copyfileobj(response, out_file)
                keysdata = scankeys()
                replace_in_file("auto-generated-env.sh", 'old', 'new')
        else:
            print("cant find keys dir ------------- success")


def init():
    directory = os.path.join(HOME, ".inflation")
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = os.path.join(HOME, ".inflation", "minion_repos")
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = os.path.join(HOME, ".inflation", "build")
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = os.path.join(HOME, ".inflation", "bin")
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = os.path.join(HOME, ".inflation", "tmp")
    if not os.path.exists(directory):
        os.makedirs(directory)

    target = os.path.abspath(os.path.join(HOME, ".inflation", "vagrantfiles"))
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

    target = os.path.abspath(os.path.join(HOME, ".inflation", "simple-vbox-server"))
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

    target = os.path.abspath(os.path.join(HOME, "inflation-master"))
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

    target = os.path.abspath(os.path.join(HOME, ".inflation", "tmp", "inflation"))

    url = "https://github.com/terminal-labs/inflation/archive/master.zip"
    filename = os.path.abspath(os.path.join(HOME, ".inflation", "tmp", "inflation.zip"))
    with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
        shutil.copyfileobj(response, out_file)
    zipfile = filename
    with ZipFile(zipfile) as zf:
        zf.extractall(".inflation/tmp/inflation")
    if os.path.exists(".inflation/tmp/inflation_resources"):
         shutil.rmtree(".inflation/tmp/inflation_resources", ignore_errors=True)
    # shutil.move(".inflation/tmp/inflation/inflation-master/inflation_resources", ".inflation/tmp/inflation_resources")
    # if os.path.exists("inflation-master/inflation_resources"):
    #     shutil.rmtree("inflation-master/inflation_resources", ignore_errors=True)
    # shutil.move(".inflation/tmp/inflation_resources", "inflation-master")
    # os.remove(filename)
    # shutil.rmtree(".inflation/tmp/inflation", ignore_errors=True)


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
