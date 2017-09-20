#!/usr/bin/env bash

source inflation_resources/scripts/header.sh

echo "stoping api server"
bash inflation_resources/scripts/server_scripts/stop_server.sh

echo "clearing debian-512mb box"
cd ~/.inflation/vbox_machine_repos/debian8-512mb
vagrant destroy -f --no-color

echo "clearing debian-1024mb box"
cd ~/.inflation/vbox_machine_repos/debian8-1024mb
vagrant destroy -f --no-color

echo "clearing debian-2048mb box"
cd ~/.inflation/vbox_machine_repos/debian8-2048mb
vagrant destroy -f --no-color

echo "clearing debian-4096mb box"
cd ~/.inflation/vbox_machine_repos/debian8-4096mb
vagrant destroy -f --no-color

echo "clearing debian-8192mb box"
cd ~/.inflation/vbox_machine_repos/debian8-8192mb
vagrant destroy -f --no-color

echo "clearing inflation dir"
rm -rf ~/.inflation

echo "clearing tmp dir"
rm -rf .tmp

echo "clearing vagrant dir"
rm -rf .vagrant

vagrant box list | grep 'There are no installed boxes! Use `vagrant box add` to add some.' &> /dev/null
if ! [ $? == 0 ]; then
  vagrant box list | cut -f 1 -d ' ' | xargs -L 1 vagrant box remove -f
fi
