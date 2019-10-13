su -m vagrant <<'EOF'
  cd /vagrant
  mkdir -p .tmp
  cd .tmp
  wget https://github.com/terminal-labs/python-environment-manager/archive/master.zip
  unzip -qq master.zip
  cp -r python-environment-manager-master/maintenance/. ../maintenance
  rm -rf python-environment-manager-master
  rm master.zip
  cd ..
  ls
EOF
