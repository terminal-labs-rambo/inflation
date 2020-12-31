import pathlib
from os.path import join, basename, abspath, isfile, dirname

package_link = ".tmp/symlink"
_path = str(pathlib.Path(__file__).parent.absolute())

def _cwd():
    return join(dirname(__file__))

def _join(a, b):
    return abspath(join(a, b))

def _split(a):
    return a.split("/")

def _backout(path):
    return _join(path, "..")

def _import_fun(mod, func):
    return getattr(__import__(mod, fromlist=[func]), func)

def _get_pgk_dir():
    currentpath = _cwd()
    i = len(currentpath.split("/"))
    while i > 0:
        currentpath = _join(currentpath, "..")
        if isfile(currentpath + "/setup.py"):
            return currentpath
            i = -1
        i = i - 1

def _get_pgk_name():
    currentpath = _cwd()
    i = len(currentpath.split("/"))
    while i > 0:
        currentpath = _join(currentpath, "..")
        if isfile(currentpath + "/setup.py"):
            return basename(currentpath).replace("-", "")
            i = -1
        i = i - 1

def setup_links(package_name):
    _link = package_link + "/"
    Path(_path + "/" + _link).mkdir(parents=True, exist_ok=True)
    if not os.path.islink(_path + "/" + _link + package_name):
        os.symlink(os.path.join(_path, _src), _path + "/" + _link + "/" + package_name)

def smart_reqs(repos, package_name):
    # styles = standalone, repo
    currentpath = _path
    def _get_deploy_style():
        currentpath = _path
        for _ in range(len(_split(currentpath))):
            currentpath = _backout(currentpath)
            if isdir(currentpath + "/.tmp/repos"):
                return "repo"

    if _get_deploy_style() == "repo":
        local_repos = os.listdir(_join(_path, ".."))
        if ".DS_Store" in local_repos:
            local_repos.remove(".DS_Store")
        if package_name in local_repos:
            local_repos.remove(package_name)

        for repo in local_repos:
            repos = [_ for _ in repos if not _.endswith(repo + ".git")]
        return repos

    return repos
