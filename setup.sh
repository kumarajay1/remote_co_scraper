sudo apt-get update 
echo "update done**************"
sudo locale-gen "en_US.UTF-8"
sudo dpkg-reconfigure --frontend noninteractive locales
echo "Locale **************"

sleep 10
sudo apt-get install python3 -y
echo "py3**************"
sudo apt-get install jq -y
sudo apt-get update 
sudo apt-get install python3-setuptools -y
echo "py3 setup tools**************"
sudo apt-get install python3-pip -y
echo "pip3**************"
sudo pip3 install pandas==0.23.4
echo "pandas**************"
sudo pip3 install selenium
echo "selenium**************"
sudo pip3 install beautifulsoup4
echo "pip3**************"
sudo pip3 install lxml
echo "pip3**************"
sudo pip3 install cassandra-driver
echo "cass**************"
sudo apt-get install firefox -y
echo "firefox**************"

