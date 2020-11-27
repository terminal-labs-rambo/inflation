su -m vagrant <<'EOF'
  cd /vagrant
  mkdir -p .tmp
  cd .tmp
  wget -O bash-environment-manager.zip https://github.com/terminal-labs/bash-environment-manager/archive/master.zip  
  unzip unzip bash-environment-manager.zip
EOF
