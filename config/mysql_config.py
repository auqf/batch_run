#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['59.46.15.210', 22, 'root', 'syszy@123'],
    ['59.46.15.211', 22, 'root', 'syszy@123']
    ]

service = [
    'yum install -y libaio numactl',
    '\cp -f /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'groupadd mysql  && useradd -g mysql  -M  -s /sbin/nologin mysql',
    'mkdir -p {/var/log/mysql_server,/home/database/mysql/data} && chown -R mysql.mysql {/var/log/mysql_server,/home/database/mysql/data}',
    'cd  /usr/local/src/mysql_package && tar xzvf mysql-glibc.tar.gz && mv mysql-glibc /usr/local/mysql',
    '\cp -f /usr/local/mysql/support-files/mysql.server  /etc/init.d/ && chmod a+x /etc/init.d/mysql.server',
    '\cp -f /usr/local/src/mysql_package/my.cnf /etc/',
    'chkconfig mysql.server on',
    'iptables -I INPUT -p tcp -m multiport --dports 3306 -j ACCEPT',
    'service iptables save',
    '/usr/local/mysql/bin/mysqld  --initialize',
    'service mysql.server start'
    ]
#'echo Please remember the following temporary password of the mysql-server for the user root@localhost',
#'cat /var/log/mysql/mysql.log |grep password |cut -d ' ' -f 13'
#alter user root@localhost identified by '';
path = {
        'src_path':'./service_src_packge/mysql_package',
        'dst_path':'/usr/local/src'
        }

service_port = 3306
