#!/usr/bin/env bash

vendor=$(<.tmp/vendor)

cd master
echo "starting salt master node"
rambo up -o ubuntu-1604
echo "master node is up"
cd ..

echo "initilising cluster"
vagrant  ssh -c "sudo bash /vagrant/inflation_resources/scripts/salt_commands.sh" 2> /dev/null
