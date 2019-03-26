#!/usr/bin/env bash

vendor=$(<.tmp/vendor)

echo "starting salt master node"
rambo up -o ubuntu-1604
echo "master node is up"

echo "initilising cluster"
vagrant  ssh -c "sudo bash /vagrant/inflation_resources/scripts/salt_commands.sh" 2> /dev/null
