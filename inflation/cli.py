import os
import sys
import json
import click
import pkg_resources

from inflation.app import (
    inflate,
    deflate,
)

PROJECT_NAME = 'inflation'
version = pkg_resources.get_distribution('inflation').version

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
def inflate_cmd():
    inflate()

### Subcommands
@cli.command('deflate')
def deflate_cmd():
    deflate()

main = cli
