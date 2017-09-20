ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')
VER=$(lsb_release -sr)
OS=$(lsb_release -si)
#if ! [ $OS == "Ubuntu"  ]
#then
#  echo "This program only works on Ubuntu 16 (or newer), existing now"
#  exit
#fi
echo "testing system for compatibility"
echo "os is" $OS
echo "architecture is" $ARCH
echo "distro version is" $VER

type virtualbox >/dev/null 2>&1 && echo "virtualbox is present." || echo "virtualbox is not $
virtualbox_version=$(vboxmanage --version)
echo "virtualbox version is"  $virtualbox_version

type vagrant >/dev/null 2>&1 && echo "vagrant is present." || echo "vagrant is not present."
vagrant_version=$(vagrant --version | head -1 | sed 's/[^0-9.]*\([0-9.]*\).*/\1/')
echo "vagrant version is"  $vagrant_version

type virtualenv >/dev/null 2>&1 && echo "virtualenv is present." || echo "virtualenv is not $
virtualenv_version=$(virtualenv --version)
echo "virtualenv version is"  $virtualenv_version

type hg >/dev/null 2>&1 && echo "mercurial is present." || echo "mercurial is not present."
mercurial_version=$(hg --version | head -1 | sed 's/[^0-9.]*\([0-9.]*\).*/\1/')
echo "mercurial version is"  $mercurial_version
echo "system looks good"
