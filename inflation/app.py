import os

from os.path import expanduser

HOME = expanduser("~")
PROJECT_LOCATION = os.path.dirname(os.path.realpath(__file__))
SALT_MASTER_RAMBO_PROJECT_LOCATION = os.path.abspath(os.path.join(PROJECT_LOCATION, '..', 'salt_master_rambo_project'))

from rambo.app import (
    up,
    destroy,
)

def inflate():
    up(vagrant_cwd=SALT_MASTER_RAMBO_PROJECT_LOCATION)

def deflate():
    destroy()
