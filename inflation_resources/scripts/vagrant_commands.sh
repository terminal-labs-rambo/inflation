#!/usr/bin/env bash

vendor=$(<.tmp/vendor)

echo "starting salt master node"
rambo up -o ubuntu-1604
rambo scp inflation_resources /vagrant/inflation_resources
rambo scp scripts /vagrant/scripts
rambo scp auth/keys /vagrant/auth/keys
rambo scp .tmp /vagrant/.tmp
rambo ssh -c "bash\ /vagrant/inflation_resources/scripts/setup_master.sh"
echo "master node is up"

echo "initilising cluster"
rambo ssh -c "sudo\ bash\ /vagrant/inflation_resources/scripts/salt_commands.sh"
