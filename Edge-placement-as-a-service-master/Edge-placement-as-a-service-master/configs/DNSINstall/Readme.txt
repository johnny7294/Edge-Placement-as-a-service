The DNS file will configure the DNS server with the entries.

The file will create ask for inputs of site name, DNS server IP, Data Center IP, Edge Web servers IP and
DNS forwarder server IP's


Site - 	give the site name. Do not include .com

The file will create the db.SITE.com file and add the appropriate lines in /etc/named.conf

access control lsit wll be added in this format 
-----------------------------------------------
acl "trusted" {
        $dns_ip;  #DNS
        $dc_ip;  #Content Server
        $edge1_ip;   #Edge1
        $edge2_ip;   #Edge2
        $forwarder_view1; #Forwarder1
		$forwarder_view2; #Forwarder2
};
acl "Edge1" {
       $forwarder_view1; #Forwarder1
	   $edge1_ip;   #Edge1
};
acl "Edge2" {
       $forwarder_view2; #Forwarder1
	   $edge2_ip;   #Edge1
};
------------------------------------------------
The edges entries will be added to www domain of the site.
The edges will be having their own views in the named.conf file.  
This view statement is responsible forreplying the Edge 1 or Edge 2 based on the forwarding DNS server.

For example the client query forwarded to the DNS server from Forwarder 1 will reply Edge 1 only for
www.SITE.com
----------------------------------------------------
view Edge2 {

        match-clients { Edge2; };
        allow-recursion { any; };

        zone "Edge2.${site}.com" {
                type master;
                file "/etc/named/db.Edge2.$site.com";
				zone-statistics yes;
                update-policy local;

        };
------------------------------------------------------
Examples:

dig Edge1.SITE.com, www.SITE.com, contentserver.SITE.com 

