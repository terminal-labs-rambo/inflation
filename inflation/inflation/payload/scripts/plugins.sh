#!/usr/bin/env bash

plugins_list=$(vagrant plugin list)

if [[ $(echo $plugins_list | grep "vagrant-aws") ]]; then
    echo "vagrant-aws is setup"
else
    vagrant plugin install vagrant-aws --no-color
fi

if [[ $(echo $plugins_list | grep "vagrant-digitalocean") ]]; then
    echo "vagrant-digitalocean is setup"
else
    vagrant plugin install vagrant-digitalocean --no-color
fi

if [[ $(echo $plugins_list | grep "vagrant-scp") ]]; then
    echo "vagrant-scp is setup"
else
    vagrant plugin install vagrant-scp --no-color  
fi
 
if [[ $(echo $plugins_list| grep "vagrant-triggers") ]]; then
    echo "vagrant-triggers is setup"
else
    vagrant plugin install vagrant-triggers --no-color 
fi
