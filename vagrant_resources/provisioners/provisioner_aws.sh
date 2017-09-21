#!/usr/bin/env bash

sudo apt update --yes -q
sudo DEBIAN_FRONTEND=noninteractive apt -y -q -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" full-upgrade

sudo cp /etc/salt/minion{,-dist}
sudo cp /vagrant/salt_resources/minions/minion.aws /etc/salt/minion
sudo cp /vagrant/salt_resources/grains/grains /etc/salt/grains
