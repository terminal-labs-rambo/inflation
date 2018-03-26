import os
import sys
import subprocess

from inflation.config_parser import process_spec_file
from rambo.app import (
    up,
    destroy,
    ssh,
    set_init_vars,
)

HOME = os.path.expanduser('~')
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_NAME = os.path.join(PROJECT_LOCATION, '..', 'salt-master-rambo-project')

def inflate(filepath):
    process_spec_file(filepath)

    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_NAME)
    up(provision=True)
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")

def deflate():
    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_NAME)
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-delete-minions.sh'")
    destroy()

def inflation_ssh():
    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_NAME)
    ssh()

def startvboxserver():
    subprocess.Popen(["python", "vbox-server.py"], cwd="/home/user/.inflation/simple-vbox-server", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stopvboxserver():
    p = subprocess.Popen(["lsof", "-t", "-i:5555"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()
    pid = output.decode("utf-8")
    
    os.system('kill ' + pid)
