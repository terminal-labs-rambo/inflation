import os
import sys
import json

import click

from keyloader.core import loadkeysdict

from inflation.app import init, inflate, deflate, inflation_ssh, startvboxserver, stopvboxserver, read_config

PROJECT_NAME = "inflation"

version = "Inflation, version 0.0.1.dev"
context_settings = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=version)
@click.pass_context
def cli(ctx):
    pass


@click.group(name="system")
def system_group():
    return None


@cli.command("init")
def init_cmd():
    init()


@cli.command("loadkeys")
def loadkeys_cmd():
    loadkeys()


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


@cli.command("startvboxserver")
def startvboxserver_cmd():
    startvboxserver()


@cli.command("stopvboxserver")
def stopvboxserver_cmd():
    stopvboxserver()


@system_group.command(name="version")
def version_command():
    print(version)


@system_group.command(name="selftest")
def selftest_command():
    print("not implemented")


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    print("not implemented")


cli.add_command(system_group)
main = cli
