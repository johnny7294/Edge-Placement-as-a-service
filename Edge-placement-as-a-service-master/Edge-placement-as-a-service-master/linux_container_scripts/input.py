import subprocess
import json
import os

#req_data = {"inputlist" : [

#{"tid" : "1","vpcid" : "1","vpcipA" : "70.150.100.2/24","vpcipB" : "70.150.100.3/24", "subid" : "1","subipA" : "172.16.10.2/24","subipB" : "172.16.10.3/24", "sub_br_ipB" : "172.15.10.4/24",},
#{"tid" : "1","vpcid" : "1","vpcipA" : "70.150.100.2/24","vpcipB" : "70.150.100.3/24", "subid" : "2","subipA" : "172.16.1.2/24","subipB" : "172.16.1.3/24", "sub_br_ipB" : "172.15.1.4/24",},
#{"tid" : "1","vpcid" : "1","vpcipA" : "70.150.100.2/24","vpcipB" : "70.150.100.3/24", "subid" : "3","subipA" : "172.16.2.2/24","subipB" : "172.16.2.3/24", "sub_br_ipB" : "172.15.2.4/24",},
#],"logging":"yes"}

req_data={"guests":[ {"name": "CS", "networks": ["T-1VPC-1SUB-1br"],"ip":"172.15.10.5/24","zone":"L2"}, { "name": "DNS", "networks": ["T-1VPC-1SUB-2br"],"ip":"172.15.1.5/24","zone":"L2"},{"name": "E1", "networks": ["T-1VPC-1SUB-3br"],"ip":"172.15.2.6/24","zone":"L2"},{"name": "E2", "networks": ["T-1VPC-1SUB-3br"],"ip":"172.15.2.5/24","zone":"L2"},{"name": "ODNS", "networks": ["tenantbr"],"ip":"10.10.10.10/24","zone":"L2"}]}

print(req_data)
if "inputlist" in req_data.keys():

    w = len(req_data["inputlist"])
    for count in range(0,w):
        req_data["inputlist"][count]["tipA"] = "90.90." + str(count) + ".2/24"
        req_data["inputlist"][count]["tipB"] = "90.90." + str(count) + ".3/24"
        req_data["inputlist"][count]["zone"] = "L2"
        #req_data["inputlist"][count]["subnetip"] = "100.100." + str(count) + ".3"
        #req_data["inputlist"][count]["dhcpstart"] = "100.100." + str(count) + ".2"
        #req_data["inputlist"][count]["dhcpend"] = "100.100." + str(count) + ".254"
    tlist=[]
    vlist=[]
    slist=[]

    for a in (req_data["inputlist"]):
        ini=str(req_data["inputlist"][req_data["inputlist"].index(a)]["zone"])+".ini"
        o="T"+a["tid"]
        if((a["tid"]!="") & (o not in tlist)):
            tlist.append("T"+a["tid"])
            data={}
            iny=[]
            iny.append(a)
            data["inputlist"]=iny
            var= json.dumps(data)
            print(req_data)
            p1= subprocess.Popen(['sudo','ansible-playbook','-i',ini,'tenant_cont.yml','-e',var])
            output=p1.communicate()[0]
            print(output)
        print(tlist)
        vp="T"+a["tid"]+"V"+a["vpcid"]
        print(vp)
        if((a["vpcid"]!="") & (vp not in vlist)):
            vlist.append(vp)
            data={}
            iny=[]
            iny.append(a)
            data["inputlist"]=iny
            var= json.dumps(data)
            print(req_data)
            p1= subprocess.Popen(['sudo','ansible-playbook','-i',ini,'vpc_cont.yml','-e',var])
            output=p1.communicate()[0]
            print(output)
        sb=vp+"S"+a["subid"]
        print(sb)
        if(a["subid"]!=""):
            data={}
            iny=[]
            iny.append(a)
            data["inputlist"]=iny
            var= json.dumps(data)
            print(req_data)
            p1= subprocess.Popen(['sudo','ansible-playbook','-i',ini,'subnet_cont.yml','-e',var])
            output=p1.communicate()[0]
            print(output)

if "guests" in req_data.keys():
    for guest in req_data["guests"]:
        ini=str(req_data["guests"][req_data["guests"].index(guest)]["zone"])+".ini"
        data={}
        iny=[]
        iny.append(guest)
        data["guests"]=iny
        var= json.dumps(data)
        p1= subprocess.Popen(['sudo','ansible-playbook','-i',ini,'end_cont.yml','-vvv','-e',var])
        output=p1.communicate()[0]
        print(output)

if "reliable" in req_data.keys():
    if req_data["reliable"]=="yes":
            print(" activated Reliablity ")

if "logging" in req_data.keys():
    if req_data["logging"]=="no":
            print(" activated Logging ")
