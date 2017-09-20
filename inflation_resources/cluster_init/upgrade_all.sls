update_aptget_db:
  module.run:
    - name: pkg.refresh_db

upgrade_all_aptget_packages:
  module.run:
    - name: pkg.upgrade

update_apt_db:
  cmd.run:
    - name: apt update

upgrade_all_apt_packages:
  cmd.run:
    - name: apt -y upgrade
