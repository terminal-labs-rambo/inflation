import os
import importlib.util

def import_mod_from_fp(module_name, filepath):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_fw = import_mod_from_fp('lib', os.path.dirname(__file__) + "/framework/lib.py")

_pgk_name = _fw.get_pkg_name()
main = _fw.import_fun(f"{_pgk_name}.cli", "
