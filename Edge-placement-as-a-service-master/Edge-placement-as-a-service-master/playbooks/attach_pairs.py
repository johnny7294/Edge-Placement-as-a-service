import sys
import subprocess
import os
import csv

container_name = sys.argv[1]
veth_pair_name = sys.argv[2]
ip_a = sys.argv[3]


print(container_name)
print(veth_pair_name)
print(ip_a)
#output = subprocess.Popen("sudo docker run --name "+str(containerb_name1)+" -itd ubuntu" ,shell=True, stdout=subprocess.PIPE)
#(out, err) = output.communicate()
#extract container ids
b_id1 = subprocess.Popen("sudo docker inspect -f '{{.State.Pid}}' "+str(container_name) ,shell=True, stdout=subprocess.PIPE)
(contb_id1, err) = b_id1.communicate()
#expose containers
output = subprocess.Popen("ln -s /proc/"+str(contb_id1)+"/ns/net /var/run/netns/"+str(contb_id1) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#attach veth to containers
output = subprocess.Popen("sudo ip link set "+veth_pair_name+" netns "+str(contb_id1) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#set veth interface up
output = subprocess.Popen("sudo ip netns exec "+str(contb_id1)+" ip link set "+veth_pair_name +" up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
#add ip
output = subprocess.Popen("sudo ip netns exec "+str(contb_id1)+" ip addr add "+str(ip_a)+" dev "+veth_pair_name ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()