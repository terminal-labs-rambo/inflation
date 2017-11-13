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
    - python
    - salt_master
