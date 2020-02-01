#Steps for creating REST API Server
1. Install Flask
2.Install virtualenv
3. cd Flask
4. source bin/activate
5. In order to run the server enter the following command:
python3 filename.py




This is how the Tenant gives input:

curl -X POST 127.0.0.1:5100/json-example -d '{"inputlist" : [
{
  "tid" : "1",
  "tipA" : "140.150.100.0/24",
  "tipB" : "150.100.10.0/24",
  "vpcid" : "1",
  "vpcipA" : "172.16.0.0/24",
  "vpcipB" : "172.16.10.0/24",
  "subid" : "1",
  "subipA" : "192.168.10.0/24",
  "subipB" : "192.168.10.10/24",
  "sub_br_ipB" : "192.168.10.30/24",
  "subnetip" : "out_of_user_subnet",
  "subnetipmask" : "255.255.255.0",
  "dhcpstart" : "192.168.0.0/24",
  "dhcpend" : "192.168.50.0/24",
  "vmname" : "content_server"}]
}' -H 'Content-Type: application/json'




The above input is only for one tenant, one VPC, one subnet.
The tenant has to replicate the same format as per his/her requirements.

{ "inputlist" :
[{
  "tid":'1',
  "tipA":'a.a.b.b',  # ip to be assigned to the vethpair connected to T-namespace
  "tipB":'a.a.b.c',  # ip to be assigned to the vethpair connected to the prov_ns
  "vpcid":'1',
  "vpcipA":'q.q.w.w.', # ip to be assigned to the vethpair connected to V-namespace
  "vpcipB":'q.q.w.e', # ip to be assigned to the vethpair connected to T-namespace
  "subid":'1',
  "subipA":'z.z.x.x', # ip to be assigned to the vethpair connected to S-namespace
  "subipB":'z.z.x.c', # ip to be assigned to the vethpair connected to V-namespace
  "sub_br_ipB":'out_of_user_subnet', # ip to be assigned to the vethpair connected from bridge to the S-namespace
  "subnetip":'out_of_user_subnet', # ip to be assigned to the bridge interface
  "subnetipmask":'255.255.255.0', 
  "dhcpstart":'out_of_user_subnet',  # starting ip of dhcp range
  "dhcpend":'out_of_user_subnet', #ending ip of dhcp range
  "vmname":'user_input'}
,{},{}......]}