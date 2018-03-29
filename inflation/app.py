import os
import sys
import shutil
import subprocess
import urllib.request
from zipfile import ZipFile

from inflation.config_parser import process_spec_file
from rambo.app import (
    up,
    destroy,
    ssh,
    set_init_vars,
)

from inflation.settings import *

def copy_auth_dir():
    target_auth_path = SALT_MASTER_RAMBO_PROJECT_LOCATION + '/auth'
    if os.path.exists(target_auth_path):
        shutil.rmtree(target_auth_path)
    if os.path.exists('auth'):
        shutil.copytree('auth', target_auth_path)
    elif os.path.exists(HOME + '/.rambo/auth'):
        shutil.copytree(HOME + '/.rambo/auth', target_auth_path)

def copy_secrets_dir():
    target_secrets_path = SALT_MASTER_RAMBO_PROJECT_LOCATION + '/secrets'
    if os.path.exists(target_secrets_path):
        shutil.rmtree(target_secrets_path)
    if os.path.exists('secrets'):
        shutil.copytree('secrets', target_secrets_path)
    elif os.path.exists(HOME + '/.rambo/secrets'):
        shutil.copytree(HOME + '/.rambo/secrets', target_secrets_path)

def init():
    directory = HOME + '/.inflation'
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + '/.inflation/minion_repos'
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + '/.inflation/build'
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = HOME + '/.inflation/bin'
    if not os.path.exists(directory):
        os.makedirs(directory)

    target = os.path.abspath(HOME + '/.inflation/vagrantfiles')
    if not os.path.exists(target): # Do not overwrite existing saltstack dir. Installs don't delete!
        url = 'https://github.com/terminal-labs/vagrantfiles/archive/master.zip'
        filename = 'vagrantfiles.zip'
        with urllib.request.urlopen(url) as response, open(
                filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath('vagrantfiles-master'), target)
        os.remove(filename)

    target = os.path.abspath(HOME + '/.inflation/simple-vbox-server')
    if not os.path.exists(target): # Do not overwrite existing saltstack dir. Installs don't delete!
        url = 'https://github.com/terminal-labs/simple-vbox-server/archive/master.zip'
        filename = 'simple-vbox-server.zip'
        with urllib.request.urlopen(url) as response, open(
                filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath('simple-vbox-server-master'), target)
        os.remove(filename)

def inflate(filepath):
    if not os.path.exists(SALT_MASTER_RAMBO_PROJECT_LOCATION):
        url = 'https://github.com/terminal-labs/sample-states/archive/inflation-master.zip'
        filename = 'inflation-master.zip'
        with urllib.request.urlopen(url) as response, open(
                filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.move(os.path.abspath('sample-states-inflation-master'), SALT_MASTER_RAMBO_PROJECT_LOCATION)
        os.remove(filename)

    copy_auth_dir()
    copy_secrets_dir()
    process_spec_file(filepath)

    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_LOCATION)
    up(provision=True)
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")

def deflate():
    if os.path.exists(SALT_MASTER_RAMBO_PROJECT_LOCATION):
        set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_LOCATION)
        ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-delete-minions.sh'")
        destroy()
        shutil.rmtree(SALT_MASTER_RAMBO_PROJECT_LOCATION)

def inflation_ssh():
    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_LOCATION)
    ssh()

def startvboxserver():
    subprocess.Popen(['python', 'vbox-server.py'], cwd=HOME + '/.inflation/simple-vbox-server', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stopvboxserver():
    p = subprocess.Popen(['lsof', '-t', '-i:5555'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()
    pid = output.decode('utf-8')

    os.system('kill ' + pid)

def createproject(project_name, config_only=None):
    path = os.path.join(os.getcwd(), project_name)
    path_exists = os.path.exists(path)
    if not path_exists:
        repo = 'sample-inflation-project'
        url = 'https://github.com/terminal-labs/sample-inflation-project/archive/master.zip'
        filename =  repo + '.zip'
        with urllib.request.urlopen(url) as response, open(
                filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall()
        shutil.copytree(os.path.abspath(repo + '-master'), path)
        shutil.rmtree(repo + '-master')
        os.remove(repo + '.zip')
    if path_exists:
        print('Directory already exists.')
