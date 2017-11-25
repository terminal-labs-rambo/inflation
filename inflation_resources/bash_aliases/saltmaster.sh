#!/usr/bin/env bash
cd /home/saltmaster/salt_controlplane
. /home/saltmaster/salt_venv/bin/activate

eval "$(ssh-agent -s)"
ssh-add /home/saltmaster/salt_controlplane/keys/master

alias inflation="python internal_cli.py"

function inflation-salt-call { # $1 = location, e.g. 'master' or '*', $2 = command
    start="su saltmaster -c \"cd /home/saltmaster; source salt_venv/bin/activate; python /home/saltmaster/salt_src/scripts/salt '"
    middle="' -c /home/saltmaster/salt_controlplane/etc/salt "
    end=" \""
    command=$start$1$middle$2$end
    eval $command
}
