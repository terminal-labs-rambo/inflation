# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import shutil
import subprocess

import distutils.dir_util
import distutils.file_util

HOME = os.path.expanduser("~")
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
MAIN_DIR = os.path.join(SCRIPT_DIR, os.pardir)

def process_file(config_file_path):
    file_obj = open(config_file_path, 'rb')
    data = file_obj.read().decode('utf-8')

    if os.path.exists('.tmp'):
        shutil.rmtree('.tmp')
    os.makedirs('.tmp')

    print('writing salt-cloud files')
    providers_section = re.compile('<start providers>(.*?)</end providers>', re.DOTALL).findall(data)[0]
    with open(MAIN_DIR + '/.tmp/cloud.providers', 'w') as outfile:
        outfile.write(providers_section)

    profiles_section = re.compile('<start profiles>(.*?)</end profiles>', re.DOTALL).findall(data)[0]
    with open(MAIN_DIR + '/.tmp/cloud.profiles', 'w') as outfile:
        outfile.write(profiles_section)

    map_section = re.compile('<start map>(.*?)</end map>', re.DOTALL).findall(data)[0]
    with open(MAIN_DIR  + '/.tmp/cloud.map', 'w') as outfile:
        outfile.write(map_section)

    vendor_section = re.compile('<start vendor>(.*?)</end vendor>', re.DOTALL).findall(data)[0]
    config = yaml.load(vendor_section)
    with open(MAIN_DIR  + '/.tmp/vendor', 'w') as outfile:
        outfile.write(config['vendor'])

    print("cloning minion repos")
    if os.path.exists(HOME + '/.inflation/minion_repos'):
        shutil.rmtree(HOME + '/.inflation/minion_repos')
    os.makedirs(HOME + '/.inflation/minion_repos')
    minion_repos_section = re.compile('<start repos>(.*?)</end repos>', re.DOTALL).findall(data)[0]
    config = yaml.load(minion_repos_section)
    for repo in config['minion_repos']:
        if '.git' in repo:
            repo_name = repo.split('/')[-1].replace('.git', '')
            cmd = 'git clone ' + repo + ' ~/.inflation/minion_repos/' + repo_name
        else:
            repo_name = repo.split('/')[-1]
            cmd = 'hg clone ' + repo + ' [name for name in os.listdir(a_dir)/' + repo_name
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        proc.communicate()[0]

    print("copying over salt state files from minion repos")
    for repo_dir in os.listdir(HOME + '/.inflation/minion_repos'):
        rambo_path = '/'
        if os.path.isdir(HOME + '/.inflation/minion_repos/' +  repo_dir + '/rambo'):
            rambo_path = '/rambo/'

        src = HOME + '/.inflation/minion_repos/' +  repo_dir + rambo_path + 'saltstack/states/.'
        dist = '.tmp/imported_salt_states/'
        distutils.dir_util.copy_tree(src, dist)
        if os.path.isfile('.tmp/imported_salt_states/top.sls'):
            os.remove('.tmp/imported_salt_states/top.sls')

    print('writing top file')
    base_section = re.compile('<start top>(.*?)</end top>', re.DOTALL).findall(data)[0]
    with open(SCRIPT_DIR + '/../.tmp/imported_salt_states/top.sls', 'w') as outfile:
        outfile.write(base_section)

    if os.path.exists('salt_master_rambo_project/.tmp'):
        shutil.rmtree('salt_master_rambo_project/.tmp')
    shutil.copytree('.tmp', 'salt_master_rambo_project/.tmp')
    shutil.rmtree('.tmp')

def main(args=None):
    config_file_path = sys.argv[1]
    process_file(config_file_path)

if __name__ == "__main__":
    main()
