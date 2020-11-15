import os
import site
import tempfile

APPDIR = os.path.abspath(os.path.dirname(__file__))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
MEMTEMPDIR = "/dev/shm"
SITEPACKAGESPATH = site.getsitepackages()[0]

if os.path.isdir(MEMTEMPDIR):
    tempfile.tempdir = MEMTEMPDIR
