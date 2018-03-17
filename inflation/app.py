import os

from inflation.config_parser import process_spec_file
from rambo.app import (
    up,
    destroy,
    set_init_vars,
)

HOME = os.path.expanduser('~')
SALT_MASTER_RAMBO_PROJECT_NAME = 'salt-master-rambo-project'

def inflate(filepath):
    working_dir = '/home/user/Desktop/inflation_system/inflation/salt-master-rambo-project'

    process_spec_file(filepath)

    set_init_vars(cwd=working_dir, tmpdir_path=working_dir)
    up(vagrant_dotfile_path=working_dir + '/.vagrant', provision=True)

def deflate():
    destroy()
