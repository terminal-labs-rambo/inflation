from inflation.derived_settings import APPDIR, SETUPFILEDIR, TESTDIR, MEMTEMPDIR, SITEPACKAGESPATH

NAME = "inflation"


def set_vars():
    VERSION = "0.0.5"
    PRINT_VERBOSITY = "high"
    EXCLUDED_DIRS = [".DS_Store"]
    SETUP_NAME = NAME
    PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
    EGG_NAME = SETUP_NAME.replace("_", "-")
    TEMPDIR = "/tmp"
    TEXTTABLE_STYLE = ["-", "|", "+", "-"]
    DIRS = [f"{TEMPDIR}/{PROJECT_NAME}"]
    MINIMUM_PYTHON_VERSION = (3, 6, 0)
    COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
    PAYLOADPATH = SITEPACKAGESPATH

    globals()["VERSION"] = VERSION
    globals()["PRINT_VERBOSITY"] = PRINT_VERBOSITY
    globals()["EXCLUDED_DIRS"] = EXCLUDED_DIRS
    globals()["SETUP_NAME"] = SETUP_NAME
    globals()["PROJECT_NAME"] = PROJECT_NAME
    globals()["EGG_NAME"] = EGG_NAME
    globals()["TEMPDIR"] = TEMPDIR
    globals()["TEXTTABLE_STYLE"] = TEXTTABLE_STYLE
    globals()["DIRS"] = DIRS
    globals()["MINIMUM_PYTHON_VERSION"] = MINIMUM_PYTHON_VERSION
    globals()["COVERAGERC_PATH"] = COVERAGERC_PATH
    globals()["SITEPACKAGESPATH"] = SITEPACKAGESPATH

    return {
        "VERSION": VERSION,
        "PRINT_VERBOSITY": PRINT_VERBOSITY,
        "EXCLUDED_DIRS": EXCLUDED_DIRS,
        "SETUP_NAME": SETUP_NAME,
        "PROJECT_NAME": PROJECT_NAME,
        "EGG_NAME": PROJECT_NAME,
        "TEMPDIR": TEMPDIR,
        "TEXTTABLE_STYLE": TEXTTABLE_STYLE,
        "DIRS": DIRS,
        "MINIMUM_PYTHON_VERSION": MINIMUM_PYTHON_VERSION,
        "COVERAGERC_PATH": COVERAGERC_PATH,
        "SITEPACKAGESPATH": SITEPACKAGESPATH,
    }


set_vars()
