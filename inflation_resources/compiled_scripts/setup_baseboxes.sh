#!/usr/bin/env bash

cd ~/.inflation/
git clone git@github.com:terminal-labs/vagrantfiles.git
cd -

  if [[ $(vboxmanage list vms | grep "ubuntu16-512mb") ]]; then
      echo "ubuntu16-512mb is setup"
  else
      mkdir -p ~/.inflation/vbox_machine_repos
      echo "setting up ubuntu16-512mb"
      cp -r ~/.inflation/vagrantfiles/ubuntu16-512mb ~/.inflation/vbox_machine_repos/ubuntu16-512mb
      cd ~/.inflation/vbox_machine_repos/ubuntu16-512mb
      vagrant up --no-color
      vagrant halt --no-color
      cd -
  fi
  if [[ $(vboxmanage list vms | grep "ubuntu16-1024mb") ]]; then
      echo "ubuntu16-1024mb is setup"
  else
      mkdir -p ~/.inflation/vbox_machine_repos
      echo "setting up ubuntu16-1024mb"
      cp -r ~/.inflation/vagrantfiles/ubuntu16-1024mb ~/.inflation/vbox_machine_repos/ubuntu16-1024mb
      cd ~/.inflation/vbox_machine_repos/ubuntu16-1024mb
      vagrant up --no-color
      vagrant halt --no-color
      cd -
  fi
  if [[ $(vboxmanage list vms | grep "ubuntu16-2048mb") ]]; then
      echo "ubuntu16-2048mb is setup"
  else
      mkdir -p ~/.inflation/vbox_machine_repos
      echo "setting up ubuntu16-2048mb"
      cp -r ~/.inflation/vagrantfiles/ubuntu16-2048mb ~/.inflation/vbox_machine_repos/ubuntu16-2048mb
      cd ~/.inflation/vbox_machine_repos/ubuntu16-2048mb
      vagrant up --no-color
      vagrant halt --no-color
      cd -
  fi
  if [[ $(vboxmanage list vms | grep "ubuntu16-4096mb") ]]; then
      echo "ubuntu16-4096mb is setup"
  else
      mkdir -p ~/.inflation/vbox_machine_repos
      echo "setting up ubuntu16-4096mb"
      cp -r ~/.inflation/vagrantfiles/ubuntu16-4096mb ~/.inflation/vbox_machine_repos/ubuntu16-4096mb
      cd ~/.inflation/vbox_machine_repos/ubuntu16-4096mb
      vagrant up --no-color
      vagrant halt --no-color
      cd -
  fi
  if [[ $(vboxmanage list vms | grep "ubuntu16-8192mb") ]]; then
      echo "ubuntu16-8192mb is setup"
  else
      mkdir -p ~/.inflation/vbox_machine_repos
      echo "setting up ubuntu16-8192mb"
      cp -r ~/.inflation/vagrantfiles/ubuntu16-8192mb ~/.inflation/vbox_machine_repos/ubuntu16-8192mb
      cd ~/.inflation/vbox_machine_repos/ubuntu16-8192mb
      vagrant up --no-color
      vagrant halt --no-color
      cd -
  fi
