import sys
import subprocess
import os
import csv

container_name = sys.argv[1]
bridge = sys.argv[2]
ip_a = sys.argv[3]


print(container_name)
print(ip_a)

#crate veth pairs
output = subprocess.Popen("sudo ip link add vethA"+container_name+" type veth peer name vethB"+container_name,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()


#extract container ids
b_id1 = subprocess.Popen("sudo docker inspect -f '{{.State.Pid}}' "+str(container_name) ,shell=True, stdout=subprocess.PIPE)
(contb_id1, err) = b_id1.communicate()
#expose containers
#output = subprocess.Popen("ln -s /proc/"+str(contb_id1)+"/ns/net /var/run/netns/"+str(contb_id1) ,shell=True, stdout=subprocess.PIPE)
#(out, err) = output.communicate()
#attach veth to containers
output = subprocess.Popen("sudo ip link set vethA"+container_name+" netns "+str(contb_id1) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#set veth interface up
output = subprocess.Popen("sudo docker exec "+str(container_name)+" ip link set vethA"+container_name+" up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#add ip
output = subprocess.Popen("sudo docker exec "+str(container_name)+" ip addr add "+str(ip_a)+" dev vethA"+container_name,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#set veth interface up
output = subprocess.Popen("sudo ip link set vethB"+container_name+" up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#add interface to bridge
output = subprocess.Popen("sudo brctl addif "+bridge+" vethB"+container_name,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
