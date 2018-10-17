#! /usr/bin/env python
# coding: utf-8

hosts = [
        ['192.168.1.176',22,'root','auqf'],
        ['172.60.1.228',22,'root','rootroot']
    ]

service = ['cd /usr/local/src/ && unzip -o srs-master.zip;cd srs-master/trunk && ./configure && make -j$(nproc) && make install',
       'ln -sf /usr/local/srs/etc/init.d/srs /etc/init.d/srs',
       'sed -i "s/__defaultVhost__/vod.ebs.com/g" /usr/local/srs/conf/dvr.segment.conf',
       'sed -i "s/30/1800/g" /usr/local/srs/conf/dvr.segment.conf',
       'sed -i "s#\./objs/nginx/html/\[app\]/\[stream\]\.#/home/ebs_dvr/\[app\]/\[stream\]_#g" /usr/local/srs/conf/dvr.segment.conf',
       'tail -n 9 /usr/local/srs/conf/dvr.segment.conf >> /usr/local/srs/conf/srs.conf',
       '/etc/init.d/srs restart',
       'echo /etc/init.d/srs start > /etc/rc.local',
       'iptables -I INPUT -p tcp -m multiport --dports 8080,1935,1985 -j ACCEPT',
       '/etc/init.d/iptables save'
]

path = {
        'src_path':'./service_src_packge/srs-master.zip',
        'dst_path':'/usr/local/src'
        }

service_port = 1935
