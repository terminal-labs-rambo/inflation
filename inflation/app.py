import os
from os.path import dirname, realpath, abspath, join, exists
from configparser import ConfigParser

from rambo.app import up, destroy, ssh
from inflation.utils import _delete_dir, _create_dir, _copy_dir, _create_dirs, _resolve_payload_path, _get_github_repo

from inflation.settings import *

HOME = "."
PROJECT_LOCATION = dirname(realpath(__file__))
inflation_master_path = abspath(join(HOME, ".tmp", "artifacts", "nucleation"))
inflation_master_tmp = abspath(join(inflation_master_path, ".tmp"))
# URLS = {
#     "GITHUBBASE": "https://github.com/terminal-labs"
# }
# PATHS = {
#     "clustermaster": abspath(join(HOME, ".inflation", "pattern", "std")),
#     "resources": abspath(join(HOME, ".inflation", "pattern", "std", "clustermaster", ".resources")),
# }
CONFIGDICT = {
    "HOME": HOME,
    "PROJECT_LOCATION": PROJECT_LOCATION,
    #"URLS": URLS,
    #"PATHS": PATHS,
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
        abspath(join(HOME, ".tmp", "vagrantfiles.zip")),
        abspath(join(HOME, ".tmp", "vagrantfiles.zip")),
        abspath(join(HOME, ".tmp"))
    )
    _get_github_repo(
        "https://github.com/terminal-labs/simple-vbox-server",
        abspath(join(HOME, ".tmp", "simple-vbox-server.zip")),
        abspath(join(HOME, ".tmp", "simple-vbox-server.zip")),
        abspath(join(HOME, ".tmp"))
    )
    _get_github_repo(
        "https://github.com/terminal-labs/nucleation",
        abspath(join(HOME, ".tmp", "nucleation.zip")),
        abspath(join(HOME, ".tmp", "nucleation.zip")),
        abspath(join(HOME, ".tmp"))
    )

    _create_dir(".tmp/artifacts")
    _copy_dir(abspath(join(HOME, ".tmp", "nucleation-master")), inflation_master_path)

    _create_dir(inflation_master_tmp)
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(HOME, ".tmp", "auth")))
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(inflation_master_tmp, "auth")))

    os.chdir(inflation_master_path)
    up(provider="virtualbox", tmpdir=inflation_master_tmp)
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir(inflation_master_path)
    destroy(provider="virtualbox", tmpdir=inflation_master_tmp)


def inflation_ssh():
    os.chdir(inflation_master_path)
    ssh(provider="virtualbox", tmpdir=inflation_master_tmp)
