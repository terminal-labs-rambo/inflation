# -*- coding: utf-8 -*-
import os
import re
import sys
import yaml
import subprocess

#from jinja2 import Environment, FileSystemLoader

import distutils.dir_util
import distutils.file_util

def main(args=None):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    main_dir = os.path.join(script_dir, os.pardir)

    file_obj = open(sys.argv[1], 'rb')
    data = file_obj.read()

    print 'writing salt-cloud files'
    providers_section = re.compile('<start providers>(.*?)</end providers>', re.DOTALL).findall(data)[0]
    with open(main_dir + '/.tmp/cloud.providers', 'w') as outfile:
        outfile.write(providers_section)

    profiles_section = re.compile('<start profiles>(.*?)</end profiles>', re.DOTALL).findall(data)[0]
    with open(main_dir + '/.tmp/cloud.profiles', 'w') as outfile:
        outfile.write(profiles_section)

    map_section = re.compile('<start map>(.*?)</end map>', re.DOTALL).findall(data)[0]
    with open(main_dir  + '/.tmp/cloud.map', 'w') as outfile:
        outfile.write(map_section)

    vendor_section = re.compile('<start vendor>(.*?)</end vendor>', re.DOTALL).findall(data)[0]
    config = yaml.load(vendor_section)
    with open(main_dir  + '/.tmp/vendor', 'w') as outfile:
        outfile.write(config['vendor'])

    print "cloning minion repos"
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
        print proc.communicate()[0]

    print "copying over salt state files from minion repos"
    homedir = os.path.expanduser('~')
    for repo_dir in os.listdir(homedir + '/.inflation/minion_repos'):
        rambo_path = '/'
        if os.path.isdir(homedir + '/.inflation/minion_repos/' +  repo_dir + '/rambo'):
            rambo_path = '/rambo/'

        src = homedir + '/.inflation/minion_repos/' +  repo_dir + rambo_path + 'salt_resources/states/.'
        dist = '.tmp/imported_salt_states/'
        distutils.dir_util.copy_tree(src, dist)
        if os.path.isfile('.tmp/imported_salt_states/top.sls'):
            os.remove('.tmp/imported_salt_states/top.sls')

    print 'writing top file'
    base_section = re.compile('<start top>(.*?)</end top>', re.DOTALL).findall(data)[0]
    with open(script_dir + '/../.tmp/imported_salt_states/top.sls', 'w') as outfile:
        outfile.write(base_section)

if __name__ == "__main__":
    main()
