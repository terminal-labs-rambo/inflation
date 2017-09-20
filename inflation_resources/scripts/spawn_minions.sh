#!/usr/bin/env bash
cd /home/saltmaster/salt_venv

echo "deploying minions, this may take a few minutes"
su saltmaster -c "source bin/activate; python /home/saltmaster/salt_src/scripts/salt-cloud -c /home/saltmaster/salt_controlplane/etc/salt -P -y -m /home/saltmaster/salt_controlplane/etc/salt/cloud.map --no-color" 
echo "minions deployed"
