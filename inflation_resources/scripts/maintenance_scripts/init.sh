#!/usr/bin/env bash

source inflation_resources/scripts/header.sh

uname | grep 'Darwin' &> /dev/null
if ! [ $? == 0 ]; then
 bash inflation_resources/scripts/install_scripts/linux_install.sh
else
 bash inflation_resources/scripts/install_scripts/mac_install.sh
fi

vagrant box list | grep 'There are no installed boxes! Use `vagrant box add` to add some.' &> /dev/null
if ! [ $? == 0 ]; then
  vagrant box list | cut -f 1 -d ' ' | xargs -L 1 vagrant box remove -f
fi

echo "creating inflation dir"
mkdir -p ~/.inflation
mkdir -p ~/.inflation/minion_repos

if [ ! -d "$HOME/.inflation/venv" ]; then
	echo "creating virtualenv"
	virtualenv $HOME/.inflation/venv
	source $HOME/.inflation/venv/bin/activate
        pip install -U setuptools
        pip install -U pip
	echo "installing requirements"
	pip install -r inflation_resources/vboxsaltdriver/requirements.txt
else
	echo "virtualenv exists"
fi

echo "creating tmp dir"
mkdir -p .tmp

bash inflation_resources/scripts/plugins.sh
bash inflation_resources/scripts/setup_baseboxes.sh
