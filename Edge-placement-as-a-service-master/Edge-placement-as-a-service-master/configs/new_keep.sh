#!/bin/bash

#W1
echo "net.ipv4.ip_nonlocal_bind = 1" >> /etc/sysctl.conf
sysctl -p
#mv /etc/dir1/dir2/dir3/{a.out,b.out}
mv /etc/keepalived/{keepalived.conf,keepalived.conf.org}

echo "! Configuration File for keepalived

global_defs {
   notification_email {
  root@webserver-01.example.com
   }
   notification_email_from root@webserver-01.example.com
   smtp_server 127.0.0.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
}

vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 101 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        172.16.4.150/24
    }
}" > /etc/keepalived/keepalived.conf

cd /etc/keepalived/ && systemctl start keepalived ; systemctl enable keepalived

