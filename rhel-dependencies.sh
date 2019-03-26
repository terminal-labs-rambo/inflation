yum -y check-update
yum -y upgrade

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E '%{rhel}').noarch.rpm
yum -y install https://$(rpm -E '%{?centos:centos}%{!?centos:rhel}%{rhel}').iuscommunity.org/ius-release.rpm

yum -y groupinstall 'Development Tools'
yum -y install wget
yum -y install git
yum -y install mercurial
