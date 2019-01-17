#! /usr/bin/env python
# coding: utf-8

hosts = [
        ['192.168.1.176',22,'root','auqf'],
        ['172.60.1.228',22,'root','rootroot']
    ]

service = [
        'yum install -y lrzsz sshpass'
        'cd /usr/local/src/init_server && tar xzvf DenyHosts-2.6.tar.gz && cd DenyHosts-2.6 && python setup.py install',
        'cd /usr/share/denyhosts && cp denyhosts.cfg-dist denyhosts.cfg && cp daemon-control /etc/init.d/daemon-control',
        '/etc/init.d/daemon-control start',
        'chkconfig daemon-control on',   
        'cp /usr/local/src/block_unauth_login.sh /home',
        'echo "* */1 * * * sh /home/block_unauth_login.sh"| crontab -',
        'yes | cp -r /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
        'echo "*/1 * * * * ntpdate 0.asia.pool.ntp.org"| crontab -',
        'ntpdate 0.asia.pool.ntp.org',
        'hwclock -w',
        'echo -e "net.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 1\nnet.ipv4.tcp_fin_timeout = 30\nnet.ipv4.tcp_keepalive_time = 1200\nnet.ipv4.tcp_max_syn_backlog = 8192\nnet.ipv4.tcp_max_tw_buckets = 5000" >> /etc/sysctl.conf',
]

path = {
        'src_path':'./init_server',
        'dst_path':'/usr/local/src'
        }

service_port = 22
