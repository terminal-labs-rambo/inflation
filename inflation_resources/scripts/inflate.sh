#!/usr/bin/env bash

source inflation_resources/scripts/header.sh

source $HOME/.inflation/venv/bin/activate

mkdir -p .tmp
mkdir -p auth/keys
mkdir -p auth/tokens

rm -rf .tmp/*

echo "loading ssh key into ssh-agent"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

echo "parsing cluster file"
file="$1"
python inflation_resources/config_parser.py $file

vendor=$(cat .tmp/vendor)
if [ "$vendor" == "digitalocean" ]
then
  echo -n $DIGITALOCEAN_TOKEN > .tmp/auth_token
fi
if [ "$vendor" == "aws" ]
then
  echo -n $AWS_ACCESS_KEY_ID > .tmp/auth_token
  echo -n $AWS_SECRET_ACCESS_KEY > .tmp/secret_auth_token
fi

bash inflation_resources/scripts/server_scripts/start_server.sh
bash inflation_resources/scripts/vagrant_commands.sh
