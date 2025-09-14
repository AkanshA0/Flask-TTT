Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt update
    sudo apt install -y python3 python3-pip
    cd /vagrant
    pip3 install -r requirements.txt
    python3 app.py
  SHELL
end
