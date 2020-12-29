import os

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
VARS = _import_fun(f"{_pgk_name}.framework.settings", "VARS")

def showlayout():
    return VARS
