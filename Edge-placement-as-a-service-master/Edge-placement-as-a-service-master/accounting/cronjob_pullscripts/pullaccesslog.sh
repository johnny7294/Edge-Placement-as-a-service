
#echo "enter the container name"
#read name
mkdir /home/Tenant1
mkdir /home/Tenant1/$1
sudo docker cp $1:/var/log/nginx/access.log /home/Tenant1/$1/access.log
 

