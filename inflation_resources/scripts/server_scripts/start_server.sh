#!/usr/bin/env bash

mkdir -p $HOME/.inflation

kill `lsof -t -i:5000`

if [[ $(virtualenv | grep  "You must provide a DEST_DIR") ]]; then
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
    server_esponse=`wget --server-response --max-redirect=0 http://127.0.0.1:5000 2>&1`
    if [[ $server_esponse == *"Connection refused"* ]]; then
        echo "starting api server"
        source $HOME/.inflation/venv/bin/activate
        python inflation_resources/vboxsaltdriver/vbox_cli_server.py &
    fi
else
    echo "you need to install virtualenv"
fi
