rambo vagrant scp ~/.ssh/id_rsa :/home/vagrant/.ssh/id_rsa
rambo vagrant scp ~/.ssh/id_rsa.pub :/home/vagrant/.ssh/id_rsa.pub
vagrant ssh -c "sudo -H -u saltmaster bash -c 'mkdir -p /home/saltmaster/salt_controlplane/etc/salt/keys'"
vagrant ssh -c "sudo -H -u root bash -c 'cp /home/vagrant/.ssh/id_rsa /home/saltmaster/salt_controlplane/etc/salt/keys/id_rsa'"
vagrant ssh -c "sudo -H -u root bash -c 'cp /home/vagrant/.ssh/id_rsa.pub /home/saltmaster/salt_controlplane/etc/salt/keys/id_rsa.pub'"
vagrant ssh -c "sudo -H -u root bash -c 'chown saltmaster /home/saltmaster/salt_controlplane/etc/salt/keys -R'"
vagrant ssh -c "sudo -H -u root bash -c 'chgrp saltmaster /home/saltmaster/salt_controlplane/etc/salt/keys -R'"
vagrant ssh -c "sudo su saltmaster -c 'cd /home/saltmaster; source salt_venv/bin/activate; python /home/saltmaster/salt_src/scripts/salt '\'*\'' state.sls cluster_init.apply_user_keys -c /home/saltmaster/salt_controlplane/etc/salt --timeout 1 --no-color'"
