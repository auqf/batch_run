#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    'yum install -y gcc gcc-c++ libjpeg-devel freetype-devel readline-devel libpng-devel libcurl-devel bzip2-devel openssl-devel libxml2-devel libtool-ltdl-devel',
    'ln -s /usr/lib64/libjpeg.so /usr/lib/libjpeg.so',
    'ln -s /usr/lib64/libpng.so /usr/lib/libpng.so',
    'groupadd www && useradd -g www -s /sbin/nologin -M www',
    'echo "/usr/local/lib" > /etc/ld.so.conf.d/source.conf && ldconfig',
    'cd /usr/local/src/nginx_php/ && tar xzvf pcre.tar.gz      && cd pcre      && ./configure  --prefix=/usr/local/pcre   && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf nginx.tar.gz     && cd nginx     && ./configure  --prefix=/usr/local/nginx  && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf libmcrypt.tar.gz && cd libmcrypt && ./configure  --libdir=/usr/lib64        && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf php-src.tar.gz   && cd php-src   && ./buildconf --force && ./configure  --prefix=/usr/local/php \
        --with-gd \
        --with-bz2 \
        --with-zlib \
        --with-curl \
        --with-iconv \
        --with-mhash \
        --enable-zip \
        --enable-fpm \
        --with-mcrypt \
        --enable-soap \
        --with-gettext \
        --without-pear \
        --enable-pcntl \
        --enable-shmop \
        --with-openssl \
        --disable-debug \
        --disable-rpath \
        --enable-shared \
        --enable-bcmath \
        --with-readline \
        --enable-sysvsem \
        --enable-sockets \
        --enable-opcache \
        --with-libxml-dir \
        --enable-mbstring \
        --without-sqlite3 \
        --enable-mbstring \
        --with-png-dir=/usr \
        --without-pdo-sqlite \
        --with-mysql=mysqlnd \
        --with-mysqli=mysqlnd \
        --enable-gd-native-ttf \
        --with-jpeg-dir=/usr/lib \
        --with-freetype-dir=/usr \
        --with-pdo-mysql=mysqlnd \
        --enable-inline-optimization \
        --with-config-file-path=/etc \
        --with-config-file-scan-dir=/etc/php.d \
    && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf phpredis.tar.gz    && cd phpredis    && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf swoole-src.tar.gz  && cd swoole-src  && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/nginx_php/ && tar xzvf zendopcache.tar.gz && cd zendopcache && phpize && ./configure && make -j$(nproc) && make install',
    '\cp -rf /usr/local/src/nginx_php/php.ini /etc/',
    '\cp -rf /usr/local/src/nginx_php/{nginx.conf,conf.d} /usr/local/nginx/conf',
    '\cp -rf /usr/local/src/nginx_php/status.html /usr/local/nginx/html',
    '\cp -rf /usr/local/src/nginx_php/php-fpm.conf /usr/local/php/etc/',
    '\cp -rf /usr/local/src/nginx_php/php-fpm.service /etc/init.d && chmod a+x /etc/init.d/php-fpm.service'
 
    
]

#'cd /usr/local/src/apache_php/ && tar xzvf mhash.tar.gz     && cd mhash     && ./configure && make -j$(nproc) && make install',
#'cd /usr/local/src/apache_php/ && tar xzvf mcrypt.tar.gz    && cd mcrypt    && LD_LIBRARY_PATH=/usr/local/lib && ./configure && make -j$(nproc) && make install',
path = {
        'src_path':'./service_src_packge/apache_php',
        'dst_path':'/usr/local/src'
        }

service_port = 80
