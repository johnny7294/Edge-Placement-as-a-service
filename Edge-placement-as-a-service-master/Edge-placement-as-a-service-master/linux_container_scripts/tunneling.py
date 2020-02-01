

bridge_name = "BRR1"
LC1= "20355"
LC2= "20741"
ip_vx_hyp1 = "10.10.22.2"
ip_vx_hyp2 = "10.10.23.2"
ip_gr_hyp1 = "10.10.7.2"
ip_gr_hyp2 = "10.10.8.2"




#vxlan
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" brctl addbr "+str(bridge_name) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip link set "+str(bridge_name)+" up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip link add vxlan0 type vxlan id 42 remote "+str(ip_vx_hyp2)+" dev vethsc41 dstport 4789" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip link set dev vxlan0 up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" brctl addif "+str(bridge_name)+" vxlan0" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip route add "+str(ip_vx_hyp2)+" via "+str(ip_vx_hyp1) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()

output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" brctl addbr "+str(bridge_name) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip link set "+str(bridge_name)+" up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip link add vxlan0 type vxlan id 42 remote "+str(ip_vx_hyp1)+" dev vethsc21 dstport 4789" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip link set dev vxlan0 up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" brctl addif BRR1 vxlan0" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip route add "+str(ip_vx_hyp1)+" via "+str(ip_vx_hyp2)+"" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()




#gre
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip tunnel add gretun1 mode gre local "+str(ip_gr_hyp1)+" remote "+str(ip_gr_hyp2) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip link set dev gretun1 up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip route add 10.10.3.0/24 dev gretun1" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()

output = subprocess.Popen("sudo ip netns exec "+str(LC1)+" ip route add 10.10.8.0/24 via 10.10.7.3" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()


output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip tunnel add gretun1 mode gre local "+str(ip_gr_hyp2)+" remote "+str(ip_gr_hyp1) ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip link set dev gretun1 up" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip route add 10.10.2.0/24 dev gretun1" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()
output = subprocess.Popen("sudo ip netns exec "+str(LC2)+" ip route add 10.10.7.0/24 via 10.10.8.3" ,shell=True, stdout=subprocess.PIPE)
(out, err) = output.communicate()











