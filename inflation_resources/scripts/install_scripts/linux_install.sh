#!/usr/bin/env bash

mkdir -p ~/.inflation
mkdir -p ~/.inflation/bin
mkdir -p ~/.inflation/build

cd ~/.inflation/build
git clone https://github.com/lastpass/lastpass-cli.git
cd lastpass-cli
cmake . && make

cp ~/.inflation/build/lastpass-cli/lpass ~/.inflation/bin/lpass
