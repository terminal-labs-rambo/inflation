# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import shutil
import subprocess

import distutils.dir_util
import distutils.file_util

HOME = "/vagrant"
SALT_MASTER_RAMBO_PROJECT_NAME = "inflation-master"
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_LOCATION = os.path.abspath(os.path.join(PROJECT_LOCATION, "..", SALT_MASTER_RAMBO_PROJECT_NAME))
CLUSTER_METADATA_DIR = SALT_MASTER_RAMBO_PROJECT_LOCATION + "/.tmp"


def get_section(data, tag):
    return re.compile("<start " + tag + ">(.*?)</end " + tag + ">", re.DOTALL).findall(data)[0]


def write_cloud_conf_file(filepath, data):
    with open(filepath, "w") as outfile:
        outfile.write(data)


def process_spec_file(config_file_path):
    file_obj = open(config_file_path, "rb")
    data = file_obj.read().decode("utf-8")

    if os.path.exists(CLUSTER_METADATA_DIR):
        shutil.rmtree(CLUSTER_METADATA_DIR)
    os.makedirs(CLUSTER_METADATA_DIR)

    print("writing salt-cloud files")
    providers_section = get_section(data, "providers")
    write_cloud_conf_file(CLUSTER_METADATA_DIR + "/cloud.providers", providers_section)

    profiles_section = get_section(data, "profiles")
    write_cloud_conf_file(CLUSTER_METADATA_DIR + "/cloud.profiles", profiles_section)

    map_section = get_section(data, "map")
    write_cloud_conf_file(CLUSTER_METADATA_DIR + "/cloud.map", map_section)

    vendor_section = get_section(data, "vendor")
    config = yaml.load(vendor_section)
    write_cloud_conf_file(CLUSTER_METADATA_DIR + "/vendor", config["vendor"])

    print("cloning minion repos")
    if os.path.exists(HOME + "/.inflation/minion_repos"):
        shutil.rmtree(HOME + "/.inflation/minion_repos")
    os.makedirs(HOME + "/.inflation/minion_repos")
    minion_repos_section = get_section(data, "repos")
    config = yaml.load(minion_repos_section)
    for repo in config["minion_repos"]:
        if ".git" in repo:
            repo_name = repo.split("/")[-1].replace(".git", "")
            cmd = "git clone " + repo + " " + HOME + "/.inflation/minion_repos/" + repo_name
        else:
            repo_name = repo.split("/")[-1]
            cmd = "hg clone " + repo + " [name for name in os.listdir(a_dir)/" + repo_name
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        proc.communicate()[0]

    print("copying over salt state files from minion repos")
    for repo_dir in os.listdir(HOME + "/.inflation/minion_repos"):
        rambo_path = "/"
        if os.path.isdir(HOME + "/.inflation/minion_repos/" + repo_dir + "/rambo"):
            rambo_path = "/rambo/"

        src = HOME + "/.inflation/minion_repos/" + repo_dir + rambo_path + "saltstack/states/."
        dist = CLUSTER_METADATA_DIR + "/imported_salt_states/"
        distutils.dir_util.copy_tree(src, dist)
        if os.path.isfile(CLUSTER_METADATA_DIR + "/imported_salt_states/top.sls"):
            os.remove(CLUSTER_METADATA_DIR + "/imported_salt_states/top.sls")

    print("writing top file")
    base_section = get_section(data, "top")
    write_cloud_conf_file(CLUSTER_METADATA_DIR + "/imported_salt_states/top.sls", base_section)


def main():
    config_file_path = sys.argv[1]
    process_spec_file(config_file_path)


if __name__ == "__main__":
    main()
