import os

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
    ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands.sh'")

def deflate():
    set_init_vars(cwd=SALT_MASTER_RAMBO_PROJECT_NAME)
    destroy()
