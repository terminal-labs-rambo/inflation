import os

from inflation.config_parser import process_spec_file
from rambo.app import (
    up,
    destroy,
)

HOME = os.path.expanduser('~')
SALT_MASTER_RAMBO_PROJECT_NAME = 'salt_master_rambo_project'
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_LOCATION = os.path.abspath(os.path.join(PROJECT_LOCATION, '..', SALT_MASTER_RAMBO_PROJECT_NAME))

def inflate(filepath):
    process_spec_file(filepath)
    up(vagrant_cwd=SALT_MASTER_RAMBO_PROJECT_LOCATION)

def deflate():
    destroy()
