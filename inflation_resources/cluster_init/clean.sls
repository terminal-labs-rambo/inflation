remove_vbox_file:
  cmd.run:
    - name: rm VBoxGuestAdditions*
    - cwd: /home/{{ grains['deescalated_user'] }}
    - runas: {{ grains['deescalated_user'] }}
    
remove_boostrape_file:
  cmd.run:
    - name: rm bootstrap-salt.sh 
    - cwd: /home/{{ grains['deescalated_user'] }}
    - runas: {{ grains['deescalated_user'] }}
