import subprocess
import json
import os
from flask import Flask, request



app = Flask(__name__)

@app.route('/json-example', methods=['POST'])
def json_example():

    if request.method == 'POST':
    	req_data = request.get_json()
        
		if "inputlist" in req_data.keys():      
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
			if req_data["reliable"]=="NO" and req_data["logging"]=="NO":
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
	        if req_data["reliable"]=="YES" and req_data["logging"]=="NO":
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
	        	print(" activated Reliablity ")
		    if req_data["logging"]=="YES" and req_data["reliable"]=="NO":
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
		    	print(" activated Logging ")
		    if req_data["reliable"]=="YES" and req_data["logging"]=="YES":
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
		    	print(" activated Reliablity ")


    return 'building...'
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5100)
