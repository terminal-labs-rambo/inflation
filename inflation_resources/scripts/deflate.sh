#!/usr/bin/env bash

source inflation_resources/scripts/header.sh

vendor=$(<.tmp/vendor)

echo "deleting minions"
TARGET=$vendor vagrant ssh -c "sudo bash /vagrant/inflation_resources/scripts/delete_minions.sh" --no-color

echo "clearing salt master"
TARGET=$vendor vagrant destroy -f --no-color

rm -rf .tmp
rm -rf .vagrant
