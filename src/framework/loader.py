import pathlib
from os.path import join, basename, abspath, isfile, dirname

def _cwd():
    return join(dirname(__file__))

def _join(a, b):
    return abspath(join(a, b))

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
