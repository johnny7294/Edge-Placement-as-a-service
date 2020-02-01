
sudo yum install epel-release
sudo yum install nginx

sudo systemctl start nginx
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
echo "nginx installed\n"
echo "enabling the service"
sudo systemctl enable nginx
./siteconf.sh
