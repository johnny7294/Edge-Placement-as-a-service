

echo "give lthe name of the Server"
read server
echo "give the ip address of the server"
read ip_addr

echo "This is $server.com on IP address " >> /usr/share/nginx/html/$server.txt
sudo rm -rf /etc/nginx/sites-available
sudo rm -rf /etc/nginx/sites-enabled
sudo rm -rf /var/www
sudo mkdir /etc/nginx/sites-available
sudo mkdir /etc/nginx/sites-enabled
sudo mkdir /var/www/
sudo mkdir /var/www/$server.com
sudo mkdir /var/www/$server.com/html
echo "adding $server.txt in /var/www"
cp /usr/share/nginx/html/$server.txt /var/www/$server.com/html/$server.txt
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup
echo "ading lines in nginx.conf"
sed -i  '#    }/a  \include /etc/nginx/sites-enabled/*.conf; server_names_hash_bucket_size 64;' /etc/nginx/nginx.conf

#sed "$ i \include /etc/nginx/sites-enabled/*.conf; server_names_hash_bucket_size 64;" >> /etc/nginx/nginx.conf
#cd /etc/nginx/sites-available
#touch /etc/nginx/sites-available/$server.com.conf
echo "server {
   listen $ip_addr:80;
   server_name $server.com www.$server.com;
#   location / {
#          resolver 127.0.0.1
#          proxy_pass         http://$server.com:80/;
#          proxy_redirect     off;
   location / {
      root /var/www/$server.com/html;
      index index.html index.htm;
      try_files $uri $uri/ =404;
   }

   error_page 500 502 503 504 /50x.html;
   location = /50x.html {
      root html;
   }
}" >> /etc/nginx/sites-available/$server.com.conf

echo "sites .com.conf has been created"
sudo ln -s /etc/nginx/sites-available/$server.com.conf /etc/nginx/sites-enabled/$server.com.conf
sudo systemctl restart nginx
echo "$ip_addr  $server.com     www.$server.com" >> /etc/hosts
sudo service nginx restart
