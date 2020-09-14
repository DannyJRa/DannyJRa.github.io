

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -

sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

sudo apt-get update && sudo apt-get install terraform

terraform version

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

az login


SOURCE: https://docs.microsoft.com/de-de/dotnet/core/install/linux-ubuntu
wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb



# Update R
https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04-quickstart


# Radian
# install released version
pip install -U radian
# to run radian
radian


#Langage Server
https://www.r-bloggers.com/setting-up-r-with-visual-studio-code-quickly-and-easily-with-the-languageserversetup-package/


install.packages("languageserver")