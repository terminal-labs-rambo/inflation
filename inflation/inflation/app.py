import os
import shutil
import urllib
import subprocess
from zipfile import ZipFile
from configparser import ConfigParser

from inflation.settings import *

#HOME = "/vagrant"
HOME = "."
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
INFLATION_MASTER_PATH = "/Users/mike/Desktop/inflation_vmware-cluster/.inflation/inflation-master"
from rambo.app import up, destroy, ssh, set_init_vars, set_vagrant_vars

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
        shutil.move(os.path.abspath(TMPDIR + "/" + filename.replace(".zip", "") + "-master"), target)
        os.remove(TMPDIR + "/" + filename)


def _create_dirs(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)


def _copy_specs():
    def _copy_ops(dirs, files, resourcesdir):
        if not os.path.exists(resourcesdir):
            os.makedirs(resourcesdir)

        for dir in dirs:
            full_path_to_target_dir = os.path.join(resourcesdir, "rootspec", dir)
            if not os.path.exists(full_path_to_target_dir):
                shutil.copytree(dir, full_path_to_target_dir)

        for file in files:
            full_path_to_target_file = os.path.join(resourcesdir, "rootspec", file)
            if not os.path.exists(full_path_to_target_file):
                shutil.copy(file, full_path_to_target_file)

    dirs = ["cluster", "extras", "nodes", "keys"]
    files = [
        "hypertop.txt",
        "anti-hypertop.txt",
    ]
    _copy_ops(dirs, files, os.path.join(METAFOOTBALL, METAFOOTBALLRESOURCES))
    _copy_ops(dirs, files, os.path.join(METAFOOTBALL, CLUSTERMASTER, CLUSTERMASTERRESOURCES))

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
    print(config.get("inflation-master", "ramboproject"))


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

    _emit_payload()
    _copy_specs()


def inflate(filepath):
    os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
    set_init_vars(
        cwd="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball",
        tmpdir_path="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball"
    )
    set_vagrant_vars(vagrant_dotfile_path="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball/.vagrant")
    up({"provider":"virtualbox", "sync_dir":"/Users/mike/Desktop/sample-project_inflation/.inm-metafootball"})

    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
    destroy()


def inflation_ssh():
    os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
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
