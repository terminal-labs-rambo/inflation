import os
from os.path import dirname, realpath, abspath, join, exists
from configparser import ConfigParser

from rambo.app import up, destroy, ssh, set_init_vars, set_vagrant_vars
from inflation.patterns.std import hydrate_patterns_std, prepare_pattern_resources_std
from inflation.utils import _delete_dir, _create_dir, _copy_dir, _create_dirs, _resolve_payload_path, _get_github_repo

from inflation.settings import *

# HOME = "/vagrant"
HOME = "."
PROJECT_LOCATION = dirname(realpath(__file__))
CONFIGFILE = "inflation.conf"
PATHS = {
    "clustermaster": abspath(join(HOME, ".inflation", "pattern", "std", "clustermaster")),
    "resources": abspath(join(HOME, ".inflation", "pattern", "std", "clustermaster", ".resources")),
}
CONFIGDICT = {
    "HOME": HOME,
    "PROJECT_LOCATION": PROJECT_LOCATION,
    "CONFIGFILE": CONFIGFILE,
    "PATHS": PATHS,
}


# def _copy_specs():
#     def _copy_ops(dirs, files, resourcesdir):
#         if not exists(resourcesdir):
#             os.makedirs(resourcesdir)
#
#         for dir in dirs:
#             full_path_to_target_dir = join(resourcesdir, "rootspec", dir)
#             if not exists(full_path_to_target_dir):
#                 shutil.copytree(dir, full_path_to_target_dir)
#
#         for file in files:
#             full_path_to_target_file = join(resourcesdir, "rootspec", file)
#             if not exists(full_path_to_target_file):
#                 shutil.copy(file, full_path_to_target_file)
#
#     dirs = ["cluster", "extras", "nodes", "keys"]
#     files = [
#         "hypertop.txt",
#         "anti-hypertop.txt",
#     ]


def in_inflation_project():
    cwd = os.getcwd()
    if exists(join(cwd, CONFIGFILE)):
        print("found inflation project ---- success")
        return True
    else:
        print("does not look like you are in an inflation project")
        return False


def read_config():
    config = ConfigParser()
    config.read(CONFIGFILE)
    print(config.get("inflation-master", "ramboproject"))


def init():
    _create_dir(join(HOME, ".inflation"))
    _create_dir(join(HOME, ".inflation", "repo"))
    _create_dir(join(HOME, ".inflation", "build"))
    _create_dir(join(HOME, ".inflation", "bin"))
    _create_dir(join(HOME, ".inflation", "tmp"))
    _create_dir(join(HOME, ".inflation", "pattern"))

    _get_github_repo(
        "https://github.com/terminal-labs/vagrantfiles/archive/master.zip",
        abspath(join(HOME, ".inflation", "repo", "vagrantfiles")),
        "vagrantfiles.zip",
    )

    _get_github_repo(
        "https://github.com/terminal-labs/simple-vbox-server/archive/master.zip",
        abspath(join(HOME, ".inflation", "repo", "simple-vbox-server")),
        "simple-vbox-server.zip",
    )

    hydrate_patterns_std(CONFIGDICT)
    prepare_pattern_resources_std(CONFIGDICT)


def resync():
    ## stash .vagrant dir
    ## stash .rambo-tmp dir
    ## delete keys dir
    ## delete patterns dir
    init()
    # hydrate_patterns_std()
    # prepare_pattern_resources_std()
    ## pop .vagrant dir
    ## pop .rambo-tmp dir


def inflate(filepath):
    # print(loadkeysdict())
    # process_spec_file(filepath)
    INFLATION_MASTER_PATH = "/Users/mike/Desktop/inflation_vmware-cluster/.inflation/inflation-master"
    os.chdir(INFLATION_MASTER_PATH)
    set_init_vars(cwd=INFLATION_MASTER_PATH, tmpdir_path="/Users/mike/Desktop/inflation_vmware-cluster/.inflation/inflation-master")
    up(provider="virtualbox")


# def inflate(filepath):
#     os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
#     set_init_vars(
#         cwd="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball",
#         tmpdir_path="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball",
#     )
#     set_vagrant_vars(vagrant_dotfile_path="/Users/mike/Desktop/sample-project_inflation/.inm-metafootball/.vagrant")
#     up({"provider": "virtualbox", "sync_dir": "/Users/mike/Desktop/sample-project_inflation/.inm-metafootball"})
#
#     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
#     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
#     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
    destroy()


def inflation_ssh():
    os.chdir("/Users/mike/Desktop/sample-project_inflation/.inm-metafootball")
    ssh()
