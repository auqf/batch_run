#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    '\cp -rf /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'rm -rf /home/eks && mv /home/eks_wangba /home/eks'
]

#path = {
        'src_path':'./service_src_packge/eks_wangba',
        'dst_path':'/home'
        }

#service_port = 1935
