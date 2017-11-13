# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'getoptlong'

load "vagrant_resources/modules.rb" # for random_tag

Vagrant.require_version ">= 1.9.7"

opts = GetoptLong.new(
  # Native Vagrant options
  [ '--force', '-f', GetoptLong::NO_ARGUMENT ],
  [ '--provision', '-p', GetoptLong::NO_ARGUMENT ],
  [ '--provision-with', GetoptLong::NO_ARGUMENT ],
  [ '--provider', GetoptLong::OPTIONAL_ARGUMENT ],
  [ '--help', '-h', GetoptLong::NO_ARGUMENT ],
  [ '--check', GetoptLong::NO_ARGUMENT ],
  [ '--logout', GetoptLong::NO_ARGUMENT ],
  [ '--token', GetoptLong::NO_ARGUMENT ],
  [ '--disable-http', GetoptLong::NO_ARGUMENT ],
  [ '--http', GetoptLong::NO_ARGUMENT ],
  [ '--https', GetoptLong::NO_ARGUMENT ],
  [ '--ssh-no-password', GetoptLong::NO_ARGUMENT ],
  [ '--ssh', GetoptLong::NO_ARGUMENT ],
  [ '--ssh-port', GetoptLong::NO_ARGUMENT ],
  [ '--ssh-once', GetoptLong::NO_ARGUMENT ],
  [ '--host', GetoptLong::NO_ARGUMENT ],
  [ '--entry-point', GetoptLong::NO_ARGUMENT ],
  [ '--plugin-source', GetoptLong::NO_ARGUMENT ],
  [ '--plugin-version', GetoptLong::NO_ARGUMENT ],
  [ '--command', '-c', GetoptLong::NO_ARGUMENT ],
  [ '--no-color', GetoptLong::NO_ARGUMENT ],
  [ '--debug', GetoptLong::NO_ARGUMENT ],

  # custom options
  [ '--target', GetoptLong::OPTIONAL_ARGUMENT ],
)

cli_target_opt=''
opts.each do |opt, arg|
  case opt
    when '--target'
      cli_target_opt=arg
  end
end

target=''
if (!ENV["TARGET"] and cli_target_opt=='') or ENV["TARGET"] == "virtualbox" or cli_target_opt == "virtualbox"
  target='virtualbox'
elsif ENV["TARGET"] == "ec2" or cli_target_opt == "ec2"
  target='ec2'
elsif ENV["TARGET"] == "digitalocean" or cli_target_opt == "digitalocean"
  target='digitalocean'
end

if target == "virtualbox" # If no param or "virtualbox"
  load File.expand_path("vagrant_resources/vagrant/Vagrantfile.virtualbox")
elsif target == "ec2"
  load File.expand_path("vagrant_resources/vagrant/Vagrantfile.ec2")
elsif target == "digitalocean"
  load File.expand_path("vagrant_resources/vagrant/Vagrantfile.digitalocean")
end

# clean up files on the host after the guest is destroyed
Vagrant.configure("2") do |config|
  config.trigger.after :destroy do
    #run "rm -rf .vagrant/"
    #run "rm -rf .tmp/"
  end
end
