import os
import sys
import shutil
import subprocess
import yaml
import urllib.request
from zipfile import ZipFile

from inflation.config_parser import process_spec_file
from rambo.app import up, destroy, ssh, set_init_vars

#HOME = "/vagrant"
HOME = "."
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
INFLATION_MASTER_PATH = "/Users/mike/Desktop/inflation_vmware-cluster/.inflation/inflation-master"


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


def validate_keys_dict():
    return True


def scankeys():
    with open("keys/keys.yaml", 'r') as stream:
        keysdata = yaml.safe_load(stream)
        print(keysdata)
        return keysdata


def loadkeysdict(verbosity="high"):
    def closure_print(data):
        print(data)

    cwd = os.getcwd()
    if in_inflation_project():
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

def _create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def _get(url, target, filename, zipname):
    if not os.path.exists(target):
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath(zipname), target)
        os.remove(filename)

def init():
    _create_dir(os.path.join(HOME, ".inflation"))
    _create_dir(os.path.join(HOME, ".inflation", "minion_repos"))
    _create_dir(os.path.join(HOME, ".inflation", "build"))
    _create_dir(os.path.join(HOME, ".inflation", "bin"))
    _create_dir(os.path.join(HOME, ".inflation", "tmp"))

    _get("https://github.com/terminal-labs/vagrantfiles/archive/master.zip",
        os.path.abspath(os.path.join(HOME, ".inflation", "vagrantfiles")),
        "vagrantfiles.zip",
        "vagrantfiles-master")

    _get("https://github.com/terminal-labs/simple-vbox-server/archive/master.zip",
        os.path.abspath(os.path.join(HOME, ".inflation", "simple-vbox-server")),
        "simple-vbox-server.zip",
        "simple-vbox-server-master")

    _get("https://github.com/terminal-labs/rambo_inflation-clustermaster/archive/master.zip",
        os.path.abspath(os.path.join(HOME, ".inflation", "inflation-master")),
        "rambo_inflation-clustermaster.zip",
        "rambo_inflation-clustermaster-master")

    # shutil.move(".inflation/tmp/inflation/inflation-master/inflation_resources", ".inflation/tmp/inflation_resources")
    # if os.path.exists("inflation-master/inflation_resources"):
    #     shutil.rmtree("inflation-master/inflation_resources", ignore_errors=True)
    # shutil.move(".inflation/tmp/inflation_resources", "inflation-master")
    # os.remove(filename)
    # shutil.rmtree(".inflation/tmp/inflation", ignore_errors=True)


def inflate(filepath):
    #print(loadkeysdict())
    #process_spec_file(filepath)
    os.chdir(INFLATION_MASTER_PATH)
    set_init_vars(cwd=INFLATION_MASTER_PATH, tmpdir_path="/Users/mike/Desktop/inflation_vmware-cluster/.inflation/inflation-master")
    up(provider="virtualbox")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir("/vagrant/inflation-master")
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
