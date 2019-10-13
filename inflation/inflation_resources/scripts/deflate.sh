#!/usr/bin/env bash

source inflation_resources/scripts/header.sh

vendor=$(<.tmp/vendor)

echo "deleting minions"
vagrant ssh -c "sudo bash /vagrant/inflation_resources/scripts/delete_minions.sh" 2> /dev/null

echo "clearing salt master"
rambo destroy

rm -rf .tmp
rm -rf .vagrant
rm -rf .rambo-tmp
