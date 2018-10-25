#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    'yum install -y lua-devel pcre-devel openssl-devel',
    'groupadd nginx && useradd -g nginx -s /sbin/nologin -M nginx',
    'cd /usr/local/src/nginx_lua && tar xzvf LuaJIT.tar.gz',
    'cd /usr/local/src/nginx_lua/LuaJIT && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_lua/ && tar xzvf nginx.tar.gz && cd nginx && export LUAJIT_LIB=/usr/local/lib \
    && export LUAJIT_INC=/usr/local/include/luajit-2.1 \
    'patch -p1 ../ngx_module/nginx_healthcheck_for_nginx_1.14+.patch' \
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
        --add-module=../ngx_module/set-misc-nginx-module \
        --add-module=../ngx_module/ngx_devel_kit --add-module=../ngx_module/lua-nginx-module \
        --add-module=../ngx_module/echo-nginx-module  --add-module=../ngx_module/redis2-nginx-module \
        --add-module=../ngx_module/nginx_upstream_check_module \ --add-module=../ngx_module/nginx_limit_speed_module-master \
    && make -j$(nproc) && make install',
    'mv -f /usr/local/src/nginx_lua/conf /usr/local/nginx/',
    'cd /usr/local/src/nginx_lua && chmod a+x nginx.service && mv nginx.service /etc/init.d/',
    'service nginx.service start',
    'chkconfig nginx.service on',
    'iptables -I INPUT -p tcp -m multiport --dports 80 -j ACCEPT',
    'service iptables save'
]
#--with-mail \
#--with-mail_ssl_module \
#--with-http_sub_module \
#--with-http_dav_module \
#--with-http_flv_module \
#--with-http_mp4_module \
#--with-http_addition_module \
#--with-http_gzip_static_module \
#--with-http_secure_link_module \
#--with-http_auth_request_module \
#--with-http_random_index_module \
#--with-cc-opt="-O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic" \
path = {
        'src_path':'./service_src_packge/nginx_lua',
        'dst_path':'/usr/local/src'
        }

service_port = 80