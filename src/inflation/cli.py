import os

import click
import pytest
import requests

with open(os.path.dirname(__file__) + "/framework/lib.py") as f:
    code = compile(f.read(), "lib.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
mod = f"{_pgk_name}.framework.layout"
showlayout = _import_fun(mod, "showlayout")

mod = f"{_pgk_name}.framework.settings"
NAME = _import_fun(mod, "NAME")
VERSION = _import_fun(mod, "VERSION")
VERSION = _import_fun(mod, "VERSION")
COVERAGERC_PATH = _import_fun(mod, "COVERAGERC_PATH")

mod = f"{_pgk_name}.framework.derived_settings"
APPDIR = _import_fun(mod, "APPDIR")
TESTDIR = _import_fun(mod, "TESTDIR")

mod = f"{_pgk_name}.app"
resync = _import_fun(mod, "resync")
inflate = _import_fun(mod, "inflate")
deflate = _import_fun(mod, "deflate")
inflation_ssh = _import_fun(mod, "inflation_ssh")

loadkeys = _import_fun(f"{_pgk_name}.stubs.domainwall", "loadkeys")

PROJECT_NAME = NAME

context_settings = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.pass_context
def cli(ctx):
    pass


@click.group(name="system")
def system_group():
    pass


# @cli.command("resync")
# def resync_cmd():
#     resync()
#
#
@cli.command("loadkeys")
def loadkeys_cmd():
    print(loadkeys())

@cli.command("inflate")
@click.argument("filepath")
def inflate_cmd(filepath):
    inflate(filepath)


@cli.command("deflate")
def deflate_cmd():
    deflate()


@cli.command("ssh")
def ssh_cmd():
    inflation_ssh()


@system_group.command(name="showlayout")
def showlayout_command():
    print(*showlayout().items(), sep='\n')


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(TESTDIR)
    pytest.main(["-x", "-v", TESTDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(APPDIR)
    pytest.main(
        [
            f"--cov-config={COVERAGERC_PATH}",
            f"--cov={_pgk_name}",
            "--cov-report",
            "term-missing",
            APPDIR,
        ]
    )


cli.add_command(system_group)
main = cli
