#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['59.46.15.212',22,'root','syszy@123']
    ]

service = [
    '\cp -rf /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'yum install -y flex mysql-devel libevent-devel libffi-devel gcc gettext xz libxslt',
    'cd /usr/local/src/atlas_package && tar xzvf glib.tar.gz  && cd glib  && ./configure --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'cd /usr/local/src/atlas_package && tar xzvf Atlas.tar.gz && cd Atlas && ./configure LDFLAGS="-lcrypto" \
        --prefix=/usr/local/mysql-proxy && make -j$(nproc) && make install'
    '\cp -rf  /usr/local/src/atlas_package/example.cnf /usr/local/mysql-proxy/conf'
]

#/usr/local/mysql-proxy/bin/mysql-proxyd -c /usr/local/mysql-proxy/conf/example.conf
path = {
        'src_path':'./service_src_packge/atlas_package',
        'dst_path':'/usr/local/src'
        }

service_port = 3306
