#!/usr/bin/env bash

apt-get install --yes --quiet ca-certificates
apt-get update
apt-get upgrade --yes

apt install --yes --quiet ca-certificates
apt update
apt upgrade --yes

apt-get install --yes mercurial
apt-get install --yes git

apt-get install --yes build-essential
apt-get install --yes linux-headers-$(uname -r)
apt-get install --yes cmake
apt-get install --yes pkg-config

apt-get install --yes openssl

apt-get install --yes libcurl3
apt-get install --yes libxml2

apt-get install --yes libssl-dev
apt-get install --yes libxml2-dev
apt-get install --yes libcurl4-openssl-dev

apt-get install --yes pinentry-curses

apt-get install --yes lxc
apt-get install --yes lxc-templates
apt-get install --yes cgroup-lite

apt-get install --yes xclip
apt-get install --yes redir
apt-get install --yes rsync
apt-get install --yes p7zip
apt-get install --yes zip
apt-get install --yes unzip
apt-get install --yes wget
apt-get install --yes curl

apt-get install --yes python-dev
apt-get install --yes python-pip
apt-get install --yes python-setuptools
apt-get install --yes python-virtualenv
apt-get install --yes python-requests

pip install --upgrade pip

mkdir -p .downloads
cd .downloads

lsb_release -sr | grep '16.04' &> /dev/null
if [ $? == 0 ]; then
  wget http://download.virtualbox.org/virtualbox/5.1.28/virtualbox-5.1_5.1.28-117968~Ubuntu~xenial_amd64.deb
  dpkg -i virtualbox-5.1_5.1.28-117968~Ubuntu~xenial_amd64.deb
fi
lsb_release -sr | grep '17.04' &> /dev/null
if [ $? == 0 ]; then
  wget http://download.virtualbox.org/virtualbox/5.1.28/virtualbox-5.1_5.1.28-117968~Ubuntu~zesty_amd64.deb
  dpkg -i virtualbox-5.1_5.1.28-117968~Ubuntu~zesty_amd64.deb
fi

wget https://releases.hashicorp.com/vagrant/2.0.0/vagrant_2.0.0_x86_64.deb
dpkg -i vagrant_2.0.0_x86_64.deb
