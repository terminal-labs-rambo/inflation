import os
import site
import tempfile


def set_vars():
    APPDIR = os.path.abspath(os.path.dirname(__file__))
    SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
    TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
    MEMTEMPDIR = "/dev/shm"
    SITEPACKAGESPATH = site.getsitepackages()[0]

    if os.path.isdir(MEMTEMPDIR):
        tempfile.tempdir = MEMTEMPDIR

    globals()["APPDIR"] = APPDIR
    globals()["SETUPFILEDIR"] = SETUPFILEDIR
    globals()["TESTDIR"] = TESTDIR
    globals()["MEMTEMPDIR"] = MEMTEMPDIR
    globals()["SITEPACKAGESPATH"] = SITEPACKAGESPATH

    return {"APPDIR": APPDIR, "SETUPFILEDIR": SETUPFILEDIR, "TESTDIR": TESTDIR, "MEMTEMPDIR": MEMTEMPDIR, "SITEPACKAGESPATH": SITEPACKAGESPATH}


set_vars()
