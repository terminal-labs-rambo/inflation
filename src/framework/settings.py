import os
import configparser

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

config = configparser.ConfigParser()
_pgk_name = _get_pgk_name()

mod = f"{_pgk_name}.framework.derived_settings"
PACKAGENAME = _import_fun(mod, "PACKAGENAME")
PACKAGEDIR = _import_fun(mod, "PACKAGEDIR")
FRAMEWORKDIR = _import_fun(mod, "FRAMEWORKDIR")
SRCDIR = _import_fun(mod, "SRCDIR")
APPDIR = _import_fun(mod, "APPDIR")
SETUPFILEDIR = _import_fun(mod, "SETUPFILEDIR")
TESTDIR = _import_fun(mod, "TESTDIR")
MEMTEMPDIR = _import_fun(mod, "MEMTEMPDIR")
SITEPACKAGESPATH = _import_fun(mod, "SITEPACKAGESPATH")

mod = f"{_pgk_name}.framework.resolved_settings"
get_env_variable = _import_fun(mod, "get_env_variable")
resolve_payload_path = _import_fun(mod, "resolve_payload_path")

config.read(PACKAGEDIR + "/setup.cfg")

VERSION = config["metadata"]["version"]
NAME = config["metadata"]["name"]

FRAMEWORK_VERSION = "0.0.1"
PROJECT_NAME = NAME
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
TEMPDIR = ".tmp/scratch"
DIRS = [f"{TEMPDIR}"]
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

# conda path
# reponame = "code"
# SETUP_NAME = reponame
# EGG_NAME = SETUP_NAME.replace("_", "-")
# PAYLOADPATH = SITEPACKAGESPATH  # noqa: F841
# server_port = 5000
# socket_host = "0.0.0.0"
# PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
# )
# MONGO_DB = PROJECT_NAME  # noqa: F821
# UPLOAD_FOLDER = "uploads"
# ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
# STATIC_DIR = os.path.join(PAYLOADPATH, "static")
# PERSISTENT_WORKING_DIRS = "stub"
# CONFIG_DIC = {
#     "POSTGRES_URL": POSTGRES_URL,
#     "POSTGRES_USER": POSTGRES_USER,
#     "POSTGRES_PW": POSTGRES_PW,
#     "POSTGRES_DB": POSTGRES_DB,
# }
# tempfile.tempdir = TEMPDIR  # noqa: F821

VARS = {
    "VERSION": VERSION,
    "NAME": NAME,
    "FRAMEWORK_VERSION": FRAMEWORK_VERSION,
    "PROJECT_NAME": PROJECT_NAME,
    "PRINT_VERBOSITY": PRINT_VERBOSITY,
    "EXCLUDED_DIRS": EXCLUDED_DIRS,
    "TEMPDIR": TEMPDIR,
    "DIRS": DIRS,
    "TEXTTABLE_STYLE": TEXTTABLE_STYLE,
    "MINIMUM_PYTHON_VERSION": MINIMUM_PYTHON_VERSION,
    "COVERAGERC_PATH": COVERAGERC_PATH,
    "PACKAGENAME": PACKAGENAME,
    "PACKAGEDIR": PACKAGEDIR,
    "FRAMEWORKDIR": FRAMEWORKDIR,
    "SRCDIR": SRCDIR,
    "APPDIR": APPDIR,
    "SETUPFILEDIR": SETUPFILEDIR,
    "TESTDIR":  TESTDIR,
    "MEMTEMPDIR": MEMTEMPDIR,
    "SITEPACKAGESPATH": SITEPACKAGESPATH,
    "CONFIG": config._sections
}
