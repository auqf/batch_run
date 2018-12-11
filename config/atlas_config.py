#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.13',22,'root','auqf']
    ]

service = [
    '\cp -rf /usr/share/zoneinfo/Asia/Chongqing  /etc/localtime',
    'yum install -y flex  lua-devel mysql-devel jemalloc-devel mysql libevent-devel libffi-devel gcc gettext-devel xz libxslt',
    'cd /usr/local/src/atlas_package && tar xJvf autoconf-2.65.tar.xz && cd autoconf-2.65 && ./configure --libdir=/usr/lib64  && make && make install',
    'cd /usr/local/src/atlas_package && tar xJvf automake-1.14.tar.xz && cd automake-1.14 && ./configure --libdir=/usr/lib64 &&  make &&  make install',
    'cd /usr/local/src/atlas_package && tar xJvf glib-2.32.2.tar.xz && cd glib-2.32.2 && ./configure --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'rpm -e --nodeps  glib2*',
    'cd /usr/local/src/atlas_package && tar xzvf Atlas.tar.gz && cd Atlas && ./configure LDFLAGS="-lcrypto" --prefix=/usr/local/mysql-proxy && make -j$(nproc) && make install',
    '\cp -rf  /usr/local/src/atlas_package/3470.cnf /usr/local/mysql-proxy/conf',
    '/usr/local/mysql-proxy/bin/mysql-proxyd 3470 start'

]
#/usr/local/mysql-proxy/bin/mysql-proxy --defaults-file=/usr/local/mysql-proxy/conf/example.cnf
path = {
        'src_path':'./service_src_packge/atlas_package',
        'dst_path':'/usr/local/src'
        }

service_port = 13470
