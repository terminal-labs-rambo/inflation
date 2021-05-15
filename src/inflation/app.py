import os

from os.path import dirname, realpath, abspath, join, exists

from rambo.app import up, destroy, ssh

with open(os.path.dirname(__file__) + "/framework/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
NAME = _import_fun(f"{_pgk_name}.framework.settings", "NAME")

_delete_dir = _import_fun(f"{_pgk_name}.utils", "_delete_dir")
_create_dir = _import_fun(f"{_pgk_name}.utils", "_create_dir")
_copy_dir = _import_fun(f"{_pgk_name}.utils", "_copy_dir")
_create_dirs = _import_fun(f"{_pgk_name}.utils", "_create_dirs")
_resolve_payload_path = _import_fun(f"{_pgk_name}.utils", "_resolve_payload_path")
_get_github_repo = _import_fun(f"{_pgk_name}.utils", "_get_github_repo")

HOME = "."
PROJECT_LOCATION = dirname(realpath(__file__))
primary_nucleation_path = abspath(join(HOME, ".tmp", "artifacts", "primary-nucleation"))
primary_nucleation_tmp = abspath(join(primary_nucleation_path, ".tmp"))
secondary_nucleation_path = abspath(join(primary_nucleation_tmp, "artifacts", "secondary-nucleation"))
secondary_nucleation_tmp = abspath(join(secondary_nucleation_path, ".tmp"))

def _prep_primary_nucleation():
    _copy_dir(abspath(join(HOME, ".tmp", "unzipped", "primary-nucleation-master")), primary_nucleation_path)
    _create_dirs(
        [
            primary_nucleation_tmp,
            primary_nucleation_tmp + "/download",
            primary_nucleation_tmp + "/artifact",
            primary_nucleation_tmp + "/bin",
            primary_nucleation_tmp + "/clone",
            primary_nucleation_tmp + "/data",
            primary_nucleation_tmp + "/repo",
            primary_nucleation_tmp + "/repos",
            primary_nucleation_tmp + "/scratch",
            primary_nucleation_tmp + "/script",
            primary_nucleation_tmp + "/symlink",
            primary_nucleation_tmp + "/unzipped",
            primary_nucleation_tmp + "/var",
        ]
    )
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(primary_nucleation_tmp, "auth")))

    _get_github_repo(
        "https://github.com/terminal-labs/secondary-nucleation",
        abspath(join(primary_nucleation_tmp, "download", "secondary-nucleation.zip")),
        abspath(join(primary_nucleation_tmp, "download", "secondary-nucleation.zip")),
        primary_nucleation_tmp + "/unzipped"
    )


def _prep_secondary_nucleation():
    _copy_dir(abspath(join(primary_nucleation_tmp, "unzipped", "secondary-nucleation-master")), secondary_nucleation_path)

    _create_dir(secondary_nucleation_tmp)
    _copy_dir(abspath(join(HOME, "auth")), abspath(join(secondary_nucleation_tmp, "auth")))


def resync():
    pass


def inflate(filepath):
    # print(loadkeysdict())
    # process_spec_file(filepath)
    _create_dir(".tmp")

    _get_github_repo(
        "https://github.com/terminal-labs/vagrantfiles",
        abspath(join(HOME, ".tmp", "download", "vagrantfiles.zip")),
        abspath(join(HOME, ".tmp", "download", "vagrantfiles.zip")),
        abspath(join(HOME, ".tmp", "unzipped"))
    )
    _get_github_repo(
        "https://github.com/terminal-labs/simple-vbox-server",
        abspath(join(HOME, ".tmp", "download", "simple-vbox-server.zip")),
        abspath(join(HOME, ".tmp", "download", "simple-vbox-server.zip")),
        abspath(join(HOME, ".tmp", "unzipped"))
    )
    _get_github_repo(
        "https://github.com/terminal-labs/primary-nucleation",
        abspath(join(HOME, ".tmp", "download", "primary-nucleation.zip")),
        abspath(join(HOME, ".tmp", "download", "primary-nucleation.zip")),
        abspath(join(HOME, ".tmp", "unzipped"))
    )

    _copy_dir(abspath(join(HOME, "auth")), abspath(join(HOME, ".tmp", "auth")))

    _create_dir(".tmp/artifacts")
    _prep_primary_nucleation()

    _create_dir(join(primary_nucleation_tmp, "artifacts"))
    _prep_secondary_nucleation()

    os.chdir(primary_nucleation_path)
    up(
        tmpdir = primary_nucleation_tmp,
        provider = 'virtualbox',
        guest_os = 'ubuntu-1604',
        ram_size = '4096',
        sync_dirs = '[["saltstack/etc", "/etc/salt"], ["saltstack/srv", "/srv"]]',
        sync_type = 'rsync',
        command = 'bash /vagrant/provision.sh',
    )
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-master.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-spawn-minions.sh'")
    #     # ssh(command="'sudo bash /vagrant/scripts/salt-cloud-commands-prepare-cluster.sh'")


def deflate():
    os.chdir(primary_nucleation_path)
    destroy(provider="virtualbox", tmpdir=primary_nucleation_tmp)


def inflation_ssh():
    os.chdir(primary_nucleation_path)
    ssh(provider="virtualbox", tmpdir=primary_nucleation_tmp)
