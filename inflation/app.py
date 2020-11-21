import os
from os.path import dirname, realpath, abspath, join, exists
from configparser import ConfigParser

from rambo.app import up, destroy, ssh
from inflation.utils import _delete_dir, _create_dir, _copy_dir, _create_dirs, _resolve_payload_path, _get_github_repo

from inflation.settings import *

HOME = "."
PROJECT_LOCATION = dirname(realpath(__file__))
URLS = {
    "GITHUBBASE": "https://github.com/terminal-labs"
}
PATHS = {
    "clustermaster": abspath(join(HOME, ".inflation", "pattern", "std")),
    "resources": abspath(join(HOME, ".inflation", "pattern", "std", "clustermaster", ".resources")),
}
CONFIGDICT = {
    "HOME": HOME,
    "PROJECT_LOCATION": PROJECT_LOCATION,
    "URLS": URLS,
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


def resync():
    pass


def inflate(filepath):
    # print(loadkeysdict())
    # process_spec_file(filepath)
    _create_dir(".tmp")
    _get_github_repo(
        "https://github.com/terminal-labs/vagrantfiles",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/vagrantfiles.zip",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/vagrantfiles.zip"
    )
    _get_github_repo(
        "https://github.com/terminal-labs/simple-vbox-server",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/simple-vbox-server.zip",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/simple-vbox-server.zip"
    )
    _get_github_repo(
        "https://github.com/terminal-labs/nucleation",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/nucleation.zip",
        "/Users/mike/Desktop/inflation_work/inflation-states/.tmp/nucleation.zip"
    )
    #INFLATION_MASTER_PATH = "."
    #os.chdir(INFLATION_MASTER_PATH)
    #up(provider="virtualbox", tmpdir="/Users/mike/Desktop/inflation_work/inflation-states/.tmp/artifacts/inflation_demo/.tmp")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    INFLATION_MASTER_PATH = "."
    os.chdir(INFLATION_MASTER_PATH)
    destroy(provider="virtualbox", tmpdir="/Users/mike/Desktop/inflation_work/inflation-states/.tmp/artifacts/inflation_demo/.tmp")


def inflation_ssh():
    INFLATION_MASTER_PATH = "."
    os.chdir(INFLATION_MASTER_PATH)
    ssh(provider="virtualbox", tmpdir="/Users/mike/Desktop/inflation_work/inflation-states/.tmp/artifacts/inflation_demo/.tmp")
