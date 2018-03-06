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
