#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    'cd /usr/local/src/redis_package && tar xzvf redis.tar.gz  && cd redis && make -j$(nproc) && make -prefix=/usr/bin/redis install',
    'mv -f /usr/local/src/redis_package/conf /usr/local/redis/conf',
    'cd /usr/local/src/redis_package && chmod a+x redis.service && mv redis.service /etc/init.d/',
    'service redis.service start',
    'chkconfig redis.service on',
    'iptables -I INPUT -p tcp -m multiport --dports 6379 -j ACCEPT',
    'service iptables save'
]

path = {
        'src_path':'./service_src_packge/redis',
        'dst_path':'/usr/local/src/'
        }

service_port = 6379