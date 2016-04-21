sudo apt-get update
sudo apt-get install openjdk-7-jdk -y
echo 'export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc

## install apache web server
sudo apt-get install apache2 -y
# make a soft link at the /var/www/html
