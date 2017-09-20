base:
  'roles:master':
    - match: grain
    - clean
    - basebox
    - basebox.symlink
    - basebox.modify_bash_env
    - network
    - network.cluster
    - users
    - salt_master
