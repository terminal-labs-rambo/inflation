import os

from os.path import dirname, realpath, abspath, join, exists
from configparser import ConfigParser

from rambo.app import up, destroy, ssh
from inflation.utils import _delete_dir, _create_dir, _copy_dir, _create_dirs, _resolve_payload_path, _get_github_repo

from inflation.settings import *

HOME = "."
PROJECT_LOCATION = dirname(realpath(__file__))
primary_nucleation_path = abspath(join(HOME, ".tmp", "artifacts", "primary-nucleation"))
primary_nucleation_tmp = abspath(join(primary_nucleation_path, ".tmp"))
secondary_nucleation_path = abspath(join(primary_nucleation_tmp, "artifacts", "secondary-nucleation"))
secondary_nucleation_tmp = abspath(join(secondary_nucleation_path, ".tmp"))
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


def _prep_primary_nucleation():
    _copy_dir(abspath(join(HOME, ".tmp", "primary-nucleation-master")), primary_nucleation_path)

    _create_dir(primary_nucleation_tmp)
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(primary_nucleation_tmp, "auth")))

    _get_github_repo(
        "https://github.com/terminal-labs/secondary-nucleation",
        abspath(join(primary_nucleation_tmp, "primary-nucleation.zip")),
        abspath(join(primary_nucleation_tmp, "primary-nucleation.zip")),
        primary_nucleation_tmp
    )


def _prep_secondary_nucleation():
    _copy_dir(abspath(join(primary_nucleation_tmp, "secondary-nucleation-master")), secondary_nucleation_path)

    _create_dir(secondary_nucleation_tmp)
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(secondary_nucleation_tmp, "auth")))


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
        "https://github.com/terminal-labs/primary-nucleation",
        abspath(join(HOME, ".tmp", "primary-nucleation.zip")),
        abspath(join(HOME, ".tmp", "primary-nucleation.zip")),
        abspath(join(HOME, ".tmp"))
    )

    _copy_dir(abspath(join(HOME, "auth")), abspath(join(HOME, ".tmp", "auth")))

    _create_dir(".tmp/artifacts")
    _prep_primary_nucleation()

    _create_dir(join(primary_nucleation_tmp, "artifacts"))
    _prep_secondary_nucleation()

    os.chdir(primary_nucleation_path)
    #up(provider="virtualbox", tmpdir=primary_nucleation_tmp)
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir(primary_nucleation_path)
    destroy(provider="virtualbox", tmpdir=primary_nucleation_tmp)


def inflation_ssh():
    os.chdir(primary_nucleation_path)
    ssh(provider="virtualbox", tmpdir=primary_nucleation_tmp)
