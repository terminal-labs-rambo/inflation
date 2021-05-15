import os

with open(os.path.dirname(__file__) + "/framework/lib.py") as f:
    code = compile(f.read(), "lib.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
main = _import_fun(f"{_pgk_name}.cli", "main")
