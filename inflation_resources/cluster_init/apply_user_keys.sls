place_user_private_key:
  file.managed:
    - name: /home/vagrant/.ssh/id_rsa
    - source: salt://keys/id_rsa
    - user: vagrant
    - group: vagrant

place_user_public_key:
  file.managed:
    - name: /home/vagrant/.ssh/id_rsa.pub
    - source: salt://keys/id_rsa.pub
    - user: vagrant
    - group: vagrant

set_user_key_perms:
  file.managed:
    - name: /home/vagrant/.ssh/id_rsa
    - mode: 600

place_ssh_config_file_for_github:
  file.managed:
    - name: /home/vagrant/.ssh/config
    - source: salt://cluster_init/ssh_config_for_github.jinja
    - template: jinja
