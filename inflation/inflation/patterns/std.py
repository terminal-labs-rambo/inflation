from os.path import isdir, join, exists

from inflation.utils import _delete_dir, _create_dir, _copy_dir, _get_github_repo

from inflation.settings import *


def hydrate_patterns_std(CONFIGDICT):
    URLS = CONFIGDICT["URLS"]
    HOME = CONFIGDICT["HOME"]
    PATHS = CONFIGDICT["PATHS"]
    tmp_inflation_std = join(HOME, ".inflation", "pattern", "std")
    files_patterns_std = join(HOME, "files", "patterns", "std")

    if not exists(tmp_inflation_std):
        if isdir(files_patterns_std):
            _copy_dir(files_patterns_std, tmp_inflation_std)
        else:
            _get_github_repo(
                URLS["GITHUBBASE"] + "/" + "inflation-pattern_rambo-clustermaster",
                PATHS["clustermaster"],
                "inflation-pattern_rambo-clustermaster.zip",
            )


def prepare_pattern_resources_std(CONFIGDICT):
    HOME = CONFIGDICT["HOME"]
    PATHS = CONFIGDICT["PATHS"]
    _delete_dir(PATHS["resources"])
    _create_dir(PATHS["resources"])
    _copy_dir(join(HOME, "keys"), join(PATHS["resources"], "keys"))
