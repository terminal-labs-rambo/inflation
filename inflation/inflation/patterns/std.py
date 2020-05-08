import os
import shutil
import urllib
import subprocess
from os.path import isdir, dirname, realpath, abspath, join, exists
from zipfile import ZipFile
from configparser import ConfigParser

from inflation.utils import _delete_dir, _create_dir, _copy_dir, _create_dirs, _resolve_payload_path, _get_github_repo

from inflation.settings import *

def hydrate_patterns_std(CONFIGDICT):
    HOME = CONFIGDICT["HOME"]
    PATHS = CONFIGDICT["PATHS"]
    tmp_inflation_std = join(HOME, ".inflation", "pattern", "std")
    files_patterns_std = join(HOME, "files", "patterns", "std")

    _create_dir(tmp_inflation_std)
    _create_dir(join(tmp_inflation_std, "minion_repos"))
    if not exists(PATHS["clustermaster"]):
        if isdir(files_patterns_std):
            _copy_dir(
                files_patterns_std,
                PATHS["clustermaster"]
            )
        else:
            _get_github_repo(
                "https://github.com/terminal-labs/inflation-pattern_rambo-clustermaster/archive/master.zip",
                PATHS["clustermaster"],
                "inflation-pattern_rambo-clustermaster.zip",
            )


def prepare_pattern_resources_std(CONFIGDICT):
    HOME = CONFIGDICT["HOME"]
    PATHS = CONFIGDICT["PATHS"]
    _delete_dir(PATHS["resources"])
    _create_dir(PATHS["resources"])
    _copy_dir(
        join(HOME, "keys"),
        join(PATHS["resources"], "keys")
    )
