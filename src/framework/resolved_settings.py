import os

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
SITEPACKAGESPATH = _import_fun(f"{_pgk_name}.framework.derived_settings", "SITEPACKAGESPATH")

_egg = ".egg-link"
_paylaod = "/payload"
_conf = "/conf.cfg"


def get_env_variable(name):
    assert isinstance(name, str) is True
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def resolve_payload_path(EGG_NAME, PROJECT_NAME):
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + _egg
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path + "/" + PROJECT_NAME + _paylaod
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path + _paylaod
    return possible_payload_path


def resolve_config_path(EGG_NAME, PROJECT_NAME):
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + _egg
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path
        return possible_payload_path + _conf
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path
        return possible_payload_path + _conf
