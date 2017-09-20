#!/usr/bin/env bash
cd /home/saltmaster/salt_controlplane
. /home/saltmaster/salt_venv/bin/activate

eval "$(ssh-agent -s)"
ssh-add /home/saltmaster/salt_controlplane/keys/master

alias inflation="python internal_cli.py"
