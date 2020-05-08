import click

from inflation.settings import *

from inflation.app import init, resync, inflate, deflate, inflation_ssh, read_config
from keyloader.core import loadkeysdict

PROJECT_NAME = "inflation"

context_settings = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.pass_context
def cli(ctx):
    pass


@click.group(name="system")
def system_group():
    return None


@cli.command("init")
def init_cmd():
    init()


@cli.command("resync")
def resync_cmd():
    resync()


@cli.command("loadkeys")
def loadkeys_cmd():
    print(loadkeysdict("keys/keys.yaml"))


@cli.command("inflate")
@click.argument("filepath")
def inflate_cmd(filepath):
    print(loadkeysdict("keys/keys.yaml"))
    read_config()
    inflate(filepath)


@cli.command("deflate")
def deflate_cmd():
    deflate()


@cli.command("ssh")
def ssh_cmd():
    inflation_ssh()


# @cli.command("startvboxserver")
# def startvboxserver_cmd():
#     startvboxserver()
#
#
# @cli.command("stopvboxserver")
# def stopvboxserver_cmd():
#     stopvboxserver()


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    print("not implemented")


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    print("not implemented")


cli.add_command(system_group)
main = cli
