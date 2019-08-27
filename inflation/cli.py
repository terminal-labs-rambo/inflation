import os
import sys
import json
import pkg_resources

import click

from inflation.app import (
    init,
    inflate,
    deflate,
    inflation_ssh,
    startvboxserver,
    stopvboxserver
)

PROJECT_NAME = 'inflation'
version = pkg_resources.get_distribution(PROJECT_NAME).version

context_settings = {
    'help_option_names': ['-h', '--help'],
}

@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=version)
@click.pass_context
def cli(ctx):
    pass

@cli.command('init')
def init_cmd():
    init()

cli.command('version')
def version_cmd():
    print("0.0.1.dev")
    
@cli.command('inflate')
@click.argument('filepath')
def inflate_cmd(filepath):
    inflate(filepath)

@cli.command('deflate')
def deflate_cmd():
    deflate()

@cli.command('ssh')
def ssh_cmd():
    inflation_ssh()

@cli.command('startvboxserver')
def startvboxserver_cmd():
    startvboxserver()

@cli.command('startvboxserver')
def startvboxserver_cmd():
    startvboxserver()

@cli.command('stopvboxserver')
def stopvboxserver_cmd():
    stopvboxserver()

main = cli
