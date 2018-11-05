#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['59.46.15.213',22,'root','syszy@123']
    ]

service = [
    'yum install -y gcc',
    'cd /usr/local/src/redis_package && tar xzvf redis.tar.gz  && cd redis && make -j$(nproc) 2>&1 /dev/null && make PREFIX=/usr/local/redis install',
    'mv -f /usr/local/src/redis_package/conf /usr/local/redis/conf',
    'cd /usr/local/src/redis_package && chmod a+x redis.service && mv redis.service /etc/init.d/',
    'service redis.service start',
    'chkconfig redis.service on',
    'iptables -I INPUT -p tcp -m multiport --dports 6379 -j ACCEPT',
    'service iptables save'
]

path = {
        'src_path':'./service_src_packge/redis_package',
        'dst_path':'/usr/local/src/'
        }

service_port = 6379
