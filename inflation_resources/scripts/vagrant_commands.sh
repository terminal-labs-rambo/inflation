#!/usr/bin/env bash

vendor=$(<.tmp/vendor)

echo "starting salt master node"
vagrant --target=$vendor up
echo "master node is up"

echo "initilising cluster"
vagrant --target=$vendor ssh -c "sudo bash /vagrant/inflation_resources/scripts/salt_commands.sh" 2> /dev/null 
