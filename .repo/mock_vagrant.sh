adduser --disabled-password --gecos "" vagrant
touch /home/vagrant/.bashrc
usermod -aG sudo vagrant

mkdir -p /vagrant
cp -a . /vagrant/
chmod 777 -R /vagrant
chown -R vagrant /vagrant

echo -e vagrant ALL=\(ALL\) NOPASSWD: ALL >> /etc/sudoers
