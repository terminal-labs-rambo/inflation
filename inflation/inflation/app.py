import os
import sys
import shutil
import subprocess
import yaml
import urllib.request
from zipfile import ZipFile

from inflation.config_parser import process_spec_file
from rambo.app import up, destroy, ssh, set_init_vars

TMPDIR = ".tmp"
HOME = ".inflation-tmp"
SALT_MASTER_RAMBO_PROJECT_NAME = os.path.join(HOME, "inflation-master")


def in_inflation_project():
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "inflation.conf")):
        print("found inflation project ---- success")
        return True
    else:
        print("does not look like you are in an inflation project")
        return False


def downloader(url, target, filename):
    if not os.path.exists(target):
        with urllib.request.urlopen(url) as response, open(os.path.join(TMPDIR, filename), "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = os.path.join(TMPDIR, filename)
        with ZipFile(zipfile) as zf:
            zf.extractall(path=TMPDIR)
        shutil.move(os.path.abspath(TMPDIR + "/" + filename.replace(".zip","") + "-master"), target)
        os.remove(TMPDIR + "/" + filename)


def init():
    dirs = [
        ".tmp",
        os.path.join(HOME, "inflation"),
        os.path.join(HOME, "inflation", "minion_repos"),
        os.path.join(HOME, "inflation", "build"),
        os.path.join(HOME, "inflation", "bin"),
        os.path.join(HOME, "inflation", "tmp"),
    ]
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

    downloader(
        "https://github.com/terminal-labs/rambo_inflation-master/archive/master.zip",
        SALT_MASTER_RAMBO_PROJECT_NAME,
        "rambo_inflation-master.zip",
    )

    downloader(
        "https://github.com/terminal-labs/vagrantfiles/archive/master.zip",
        os.path.abspath(os.path.join(HOME, "inflation", "vagrantfiles")),
        "vagrantfiles.zip",
    )

    downloader(
        "https://github.com/terminal-labs/simple-vbox-server/archive/master.zip",
        os.path.abspath(os.path.join(HOME, "inflation", "simple-vbox-server")),
        "simple-vbox-server.zip",
    )

def inflate(filepath):
    #process_spec_file(filepath)
    user_cwd = os.getcwd()
    os.chdir(SALT_MASTER_RAMBO_PROJECT_NAME)
    set_init_vars(cwd= os.path.join(user_cwd, SALT_MASTER_RAMBO_PROJECT_NAME))
    up(provider="virtualbox")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    user_cwd = os.getcwd()
    os.chdir(SALT_MASTER_RAMBO_PROJECT_NAME)
    set_init_vars(cwd=os.path.join(user_cwd, SALT_MASTER_RAMBO_PROJECT_NAME))
    destroy()


def inflation_ssh():
    user_cwd = os.getcwd()
    os.chdir(SALT_MASTER_RAMBO_PROJECT_NAME)
    set_init_vars(cwd=os.path.join(user_cwd, SALT_MASTER_RAMBO_PROJECT_NAME))
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
