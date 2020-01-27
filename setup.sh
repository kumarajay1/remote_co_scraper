sudo apt-get update 
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
sleep 10
sudo apt-get install python3 -y
sudo apt-get install jq -y
sudo apt-get install python3-setuptools -y
sudo apt-get install python3-pip -y
sudo pip3 install pandas==0.23.4
sudo pip3 install selenium
sudo pip3 install beautifulsoup4
sudo pip3 install lxml
sudo pip3 install cassandra-driver
sudo apt-get install firefox -y
