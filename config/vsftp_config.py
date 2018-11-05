#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    '\cp -rf /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'yum install -y vsftpd db4 db4-utils',
    'mkdir -p /home/sample && chmod 755 /home && chmod -R 777 /home/sample'
    'groupadd vsftpd && useradd -g vsftpd -s /sbin/nologin -M vsftpd',
    '\cp -rf /usr/local/src/vsftpd_package/* /etc/vsftpd/',
    'db_load  -T -t hash -f /etc/vsftpd/vuser_passwd  /etc/vsftpd/vuser_passwd.db',
    'service vsftpd start',
    'chkconfig vsftpd on',
    'iptables -I INPUT -p tcp -m multiport --dports 20,21,40000:40010 -j ACCEPT',
    'service iptables save'
    
]

path = {
        'src_path':'./service_src_packge/vsftpd_package',
        'dst_path':'/ur/local/src/'
        }

service_port = 21
