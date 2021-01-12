# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  config.vm.box = "hashicorp/bionic64"
  config.vm.hostname = "fastapi"
  config.vm.network "private_network", ip: "192.168.50.10"
  config.vm.provision "shell", path: "bootstrap.sh"

end
