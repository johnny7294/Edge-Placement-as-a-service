#!/bin/bash

echo "Welcome to the CDN DNS installation... "
echo "Please enter the site that you want this machine to be DNS server"
read site
echo "enter the ip address on which the DNS should listen for queries"
read dns_ip
echo "enter the site's Data server's IP"
read dc_ip
echo "enter edge1 web server floating ip"
read egde1_ip
echo "enter edge2 web server floating ip"
read edge2_ip
echo "enter DNS forwarder ip for which the response is edge 1"
read forwarder_view1
echo "enter DNS forwarder ip for which the response is edge 2"
read forwarder_view2
sudo yum install bind bind-utils
echo "--------------------------------------------------------------------"
echo "bind installed editing named.conf"
sed -i '/options {/i 
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
' /etc/named.conf
sed -i '/listen-on port 53 { 127.0.0.1; /a $dns_ip;' /etc/named.conf
sed -i '/options {/ i statistics-channels { inet 127.0.0.1 port 8053 allow { 127.0.0.1; };};' /etc/named.conf
sed -i '/ allow-query     { localhost; /a any;' /etc/named.conf
sed -i ' / logging { / a channel queries {
                file "named.log" versions 3 size 5m;
                severity info;
                print-time yes;
                print-category yes;
                print-severity yes;
 };
category queries { queries;};' /etc/named.conf
sed -i ' / zone "." IN { /i         zone  "$site.com" {
                type master;
                check-names ignore;
                file "/etc/named/db.$site.com";
                update-policy local;
                zone-statistics yes;
        };' /etc/named.conf

sed -i ' /zone "." IN { /i         zone   "0.0.127.in-addr.arpa" IN {
                type master;
                file "/etc/named/zones/db.127.0.0";
                zone-statistics yes;
        };' /etc/named.conf

sed -i 'include "/etc/named.rfc1912.zones"; /i view Edge1 {
        match-clients { Edge1; };
        allow-recursion { any; };

        zone "Edge1.${site}.com" {
                type master;
                file "/etc/named/db.Edge1.$site.com";
				zone-statistics yes;
                update-policy local;

        };

};' /etc/named.conf


sed -i 'include "/etc/named.rfc1912.zones"; /i view Edge2 {

        match-clients { Edge1; };
        allow-recursion { any; };

        zone "Edge2.${site}.com" {
                type master;
                file "/etc/named/db.Edge2.$site.com";
				zone-statistics yes;
                update-policy local;

        };

};' /etc/named.conf

echo "named.conf edited"
dnsdbfile=/etc/named/db.$site.com
localdnsfile=/etc/named/db.127.0.0
edge1dbfile=/etc/named/db.Edge1.$site.com
edge2dbfile=/etc/named/db.Edge2.$site.com
cp /var/named/named.empty $localdnsfile
sed "s/3H/24000/g"$localdnsfile > $localdnsfile
sed "s/rname.invalid./localhost. root.localhost./g"$localdnsfile > $localdnsfile
sed "s/ 0       ; serial/ 2       ; serial/g"$localdnsfile > $localdnsfile
sed "s/ 1D      ; refresh/ 24000      ; refresh/g"$localdnsfile > $localdnsfile
sed "s/ 1H      ; retry/ 12000      ; retry/g"$localdnsfile > $localdnsfile
sed -i 's/         NS      @
        A       127.0.0.1
        AAAA    ::1
/@                IN      NS      localhost.
1.0.0            IN      PTR     localhost.
/g' $localdnsfile

echo "adding dns db file"
cp /var/named/named.empty $dnsdbfile
sed "s/3H/24000/g"$dnsdbfile > $dnsdbfile
sed "s/rname.invalid./ns1.$site.com./g"$dnsdbfile > $dnsdbfile
sed "s/ 1D      ; refresh/ 24000      ; refresh/g"$dnsdbfile > $dnsdbfile
sed "s/ 1H      ; retry/ 12000      ; retry/g"$dnsdbfile > $dnsdbfile
sed "s/ 0       ; serial/ 2       ; serial/g"$dnsdbfile > $dnsdbfile
sed -i '/AAAA    ::1/a 
@       IN      NS      ns1.$site.com.
@       IN      A       $dns_ip
ns1     IN      A       $dns_ip
Edge1                   IN      A       egde1_ip
Edge2                   IN      A       egde2_ip
forwarder1              IN      A       forwarder_view1
forwarder2              IN      A       forwarder_view2
contentserver           IN      A       dc_ip
www     IN      CNAME   contentserver.$site.com.
$site.com.       IN      TXT     "Hello $site.com is up"' $dnsdbfile

echo "added dns db file"
cp $dnsdbfile $edge1dbfile
sed "s/contentserver.$site.com./Edge1.$site.com./g"$edge1dbfile > $edge1dbfile
sed "s/contentserver.$site.com./Edge2.$site.com./g"$edge2dbfile > $edge2dbfile

echo "added edge1 and edge2 db file"
sudo service named stop
sudo service named start
echo "done !!!!!"