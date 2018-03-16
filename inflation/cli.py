import os
import sys
import json
import pkg_resources

import click

from inflation.app import (
    inflate,
    deflate,
)

PROJECT_NAME = 'inflation'
version = pkg_resources.get_distribution(PROJECT_NAME).version

context_settings = {
    'help_option_names': ['-h', '--help'],
}

### Main command / CLI entry point
@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=version)
@click.pass_context
def cli(ctx):
    pass

### Subcommands
@cli.command('inflate')
@click.argument('filepath')
def inflate_cmd(filepath):
    inflate(filepath)

### Subcommands
@cli.command('deflate')
def deflate_cmd():
    deflate()

main = cli
