import os

VERSION='0.0.5.dev'
PROJECT_NAME = 'inflation'
HOME = os.path.expanduser('~')
SALT_MASTER_RAMBO_PROJECT_NAME = '.inflation-master'
SALT_MASTER_RAMBO_PROJECT_LOCATION = os.path.abspath(os.path.join(os.path.realpath(os.getcwd()), SALT_MASTER_RAMBO_PROJECT_NAME))
CLUSTER_METADATA_DIR = SALT_MASTER_RAMBO_PROJECT_LOCATION + '/.tmp'
