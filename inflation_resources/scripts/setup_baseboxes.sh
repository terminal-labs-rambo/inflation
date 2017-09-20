#!/usr/bin/env bash

cd ~/.inflation/
git clone git@github.com:terminal-labs/vagrantfiles.git
cd -

if [[ $(vboxmanage list vms | grep "debian8-512mb") ]]; then
    echo "debian8-512mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up debian8-512mb"
    cp -r ~/.inflation/vagrantfiles/debian8-512mb ~/.inflation/vbox_machine_repos/debian8-512mb
    cd ~/.inflation/vbox_machine_repos/debian8-512mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "debian8-1024mb") ]]; then
    echo "debian8-1024mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up debian8-1024mb"
    cp -r ~/.inflation/vagrantfiles/debian8-1024mb ~/.inflation/vbox_machine_repos/debian8-1024mb
    cd ~/.inflation/vbox_machine_repos/debian8-1024mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "debian8-2048mb") ]]; then
    echo "debian8-2048mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up debian8-2048mb"
    cp -r ~/.inflation/vagrantfiles/debian8-2048mb ~/.inflation/vbox_machine_repos/debian8-2048mb
    cd ~/.inflation/vbox_machine_repos/debian8-2048mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "debian8-4096mb") ]]; then
    echo "debian8-4096mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up debian8-4096mb"
    cp -r ~/.inflation/vagrantfiles/debian8-4096mb ~/.inflation/vbox_machine_repos/debian8-4096mb
    cd ~/.inflation/vbox_machine_repos/debian8-4096mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "debian8-8192mb") ]]; then
    echo "debian8-8192mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up debian8-8192mb"
    cp -r ~/.inflation/vagrantfiles/debian8-8192mb ~/.inflation/vbox_machine_repos/debian8-8192mb
    cd ~/.inflation/vbox_machine_repos/debian8-8192mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "ubuntu14-512mb") ]]; then
    echo "ubuntu14-512mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up ubuntu14-512mb"
    cp -r ~/.inflation/vagrantfiles/ubuntu14-512mb ~/.inflation/vbox_machine_repos/ubuntu14-512mb
    cd ~/.inflation/vbox_machine_repos/ubuntu14-512mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "ubuntu14-1024mb") ]]; then
    echo "ubuntu14-1024mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up ubuntu14-1024mb"
    cp -r ~/.inflation/vagrantfiles/ubuntu14-1024mb ~/.inflation/vbox_machine_repos/ubuntu14-1024mb
    cd ~/.inflation/vbox_machine_repos/ubuntu14-1024mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "ubuntu14-2048mb") ]]; then
    echo "ubuntu14-2048mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up ubuntu14-2048mb"
    cp -r ~/.inflation/vagrantfiles/ubuntu14-2048mb ~/.inflation/vbox_machine_repos/ubuntu14-2048mb
    cd ~/.inflation/vbox_machine_repos/ubuntu14-2048mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "ubuntu14-4096mb") ]]; then
    echo "ubuntu14-4096mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up ubuntu14-4096mb"
    cp -r ~/.inflation/vagrantfiles/ubuntu14-4096mb ~/.inflation/vbox_machine_repos/ubuntu14-4096mb
    cd ~/.inflation/vbox_machine_repos/ubuntu14-4096mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi

if [[ $(vboxmanage list vms | grep "ubuntu14-8192mb") ]]; then
    echo "ubuntu14-8192mb is setup"
else
    mkdir -p ~/.inflation/vbox_machine_repos
    echo "setting up ubuntu14-8192mb"
    cp -r ~/.inflation/vagrantfiles/ubuntu14-8192mb ~/.inflation/vbox_machine_repos/ubuntu14-8192mb
    cd ~/.inflation/vbox_machine_repos/ubuntu14-8192mb
    vagrant up --no-color
    vagrant halt --no-color
    cd -
fi
