# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu-14.04-amd64-vbox"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"

  config.vm.network "forwarded_port", guest: 5000, host: 5001
  config.vm.network "forwarded_port", guest: 80, host: 8080
  #config.vm.network "forwarded_port", guest: 27017, host: 27017
  #config.vm.network "private_network", ip: "10.1.1.10"

  config.vm.provider "virtualbox" do |vb|
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

  config.vm.provision "shell", inline: "apt-get -y remove grub-legacy grub-common"
  config.vm.provision "shell", inline: "apt-get update"
  #config.vm.provision "shell", inline: "apt-get -y upgrade"
  config.vm.provision "shell", inline: "curl -s https://get.docker.io/ubuntu/ | sh"
  config.vm.provision "shell", inline: "sudo usermod -G docker -a 'vagrant'"
  #config.vm.provision "shell", inline: "apt-get install -y mongodb-org"

  config.vm.provision "shell", inline: "docker run -d -p 80:80 \
      -v /var/run/docker.sock:/tmp/docker.sock jwilder/nginx-proxy"
end
