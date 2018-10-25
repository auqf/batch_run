#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    'cp -f /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'groupadd mysql  && useradd -g mysql  -M  -s /sbin/nologin mysql',
    'mkdir -p {/var/log/mysql_server,/home/database/mysql/data} && chown -R mysql.mysql {/var/local/mysql_server, /home/database/mysql/data}',
    'cp -f /usr/local/mysql/support-files/mysql.server  /etc/init.d/',
    'cd  /usr/local/src/mysql_package && tar xzvf mysql-glibc.tar.gz && cd mysql-glibc',
    'cp /usr/local/src/mysql_package/my.cnf /etc/',
    '/usr/local/mysql/bin/mysqld  --initialize',
    'service mysql.server start',
    'chkconfig mysql.server on',
    'iptables -I INPUT -p tcp -m multiport --dports 3306 -j ACCEPT',
    'service iptables save',
    
    ]
#'echo Please remember the following temporary password of the mysql-server for the user root@localhost',
#'cat /var/log/mysql/mysql.log |grep password |cut -d ' ' -f 13'
#alter user root@localhost identified by '';
path = {
        'src_path':'./service_src_packge/mysql_package',
        'dst_path':'/usr/local/src'
        }

service_port = 3306
