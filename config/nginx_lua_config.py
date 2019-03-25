#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.221',22,'root','vlang@123'],
    ]

service = [
    'yum install -y lua-devel pcre-devel openssl-devel',
    'groupadd nginx > /dev/null 2>&1 && useradd -g nginx -s /sbin/nologin -M nginx > /dev/null 2>&1',
    'cd /usr/local/src/nginx_lua && tar xzvf LuaJIT.tar.gz && cd LuaJIT && make -j$(nproc) && make install && echo "/usr/local/lib/" >>  /etc/ld.so.conf && ldconfig',
    'cd /usr/local/src/nginx_lua/ && tar xzvf nginx.tar.gz && cd nginx \
    && export LUAJIT_LIB=/usr/local/lib && export LUAJIT_INC=/usr/local/include/luajit-2.1 \
    && ./configure \
        --user=nginx \
        --group=nginx \
        --with-stream \
        --with-file-aio \
        --with-http_v2_module \
        --with-http_ssl_module \
        --with-http_gunzip_module \
        --with-http_realip_module \
        --with-http_stub_status_module \
        --add-module=../ngx_module/ngx_devel_kit \
        --add-module=../ngx_module/set-misc-nginx-module --add-module=../ngx_module/lua-nginx-module \
        --add-module=../ngx_module/echo-nginx-module  --add-module=../ngx_module/redis2-nginx-module \
        --add-module=../ngx_module/ngx_healthcheck_module \
        --add-module=../ngx_module/nginx_limit_speed_module-master \
    && make -j$(nproc) && make install',
    '\cp -r /usr/local/src/nginx_lua/conf /usr/local/nginx/',
    'cd /usr/local/src/nginx_lua && chmod a+x nginx.service && mv nginx.service /etc/init.d/',
    'service nginx.service start',
    'chkconfig nginx.service on',
    'iptables -I INPUT -p tcp -m multiport --dports 80 -j ACCEPT',
    'service iptables save'
]
#&& patch -p1 ../ngx_module/ngx_healthcheck_module/nginx_healthcheck_for_nginx_1.14+.patch \
path = {
        'src_path':'./service_src_packge/nginx_lua',
        'dst_path':'/usr/local/src'
        }

service_port = 80
