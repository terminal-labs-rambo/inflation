#!/usr/bin/env bash
cd /home/saltmaster/salt_venv

echo "deleting minions, this may take a few minutes"
su saltmaster -c "source bin/activate; salt-cloud -c /home/saltmaster/salt_controlplane/etc/salt -y -m /home/saltmaster/salt_controlplane/etc/salt/cloud.map -d --no-color"
echo "minions deleted"