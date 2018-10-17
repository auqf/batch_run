#! /usr/bin/env python
# coding: utf-8

hosts = [
        ['192.168.1.176',22,'root','auqf'],
        ['172.60.1.228',22,'root','rootroot']
    ]

service = [
        'pwd',
        'ls -lhrt ./'
]

path = {
        'src_path':'./service_src_packge/srs-master.zip',
        'dst_path':'/usr/local/src'
        }

service_port = 935
