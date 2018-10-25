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
    'groupadd apache && useradd -g apache -s /sbin/nologin -M apache',
    'echo "/usr/local/lib" > /etc/ld.so.conf.d/source.conf && ldconfig',
    'cd /usr/local/src/apache_php/ && tar xzvf pcre.tar.gz     &&  cd pcre     && ./configure  --prefix=/usr/local/pcre   && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf apr.tar.gz      &&  cd apr      && ./configure  --prefix=/usr/local/apr    && make -j$(nproc) && make install',
    "cd /usr/local/src/apache_php/ && tar xzvf apr-util.tar.gz &&  cd apr-util && ./configure  --with-apr=/usr/local/apr  && make -j$(nproc) && make install",
    'cd /usr/local/src/apache_php/ && tar xzvf httpd.tar.gz    &&  cd httpd    && ./configure --prefix=/usr/local/apache \
        --enable-headers \
        --enable-rewrite  \
        --disable-userdir \
        --disable-cgid \
        --disable-cgi \
        --with-pcre=/usr/local/pcre \
        --enable-so \
        --with-ssl \
        --enable-ssl \
        --with-apr=/usr/local/apr \
        --with-apr-util=/usr/local/apr \
        --with-share \
        --enable-mpms-shared=all  \
        --enable-info  \
        --with-crypto \
        && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf libmcrypt.tar.gz && cd libmcrypt && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf mhash.tar.gz     && cd mhash     && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf mcrypt.tar.gz    && cd mcrypt    && LD_LIBRARY_PATH=/usr/local/lib && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf php-src.tar.gz   && cd php-src   && ./configure \
        --enable-inline-optimization \
        --disable-debug \
        --disable-rpath \
        --enable-shared \
        --enable-opcache \
        --with-mysql=mysqlnd \
        --with-mysqli=mysqlnd \
        --with-pdo-mysql=mysqlnd \
        --with-gettext \
        --enable-mbstring \
        --with-iconv \
        --with-mcrypt \
        --with-mhash \
        --with-openssl \
        --enable-bcmath \
        --enable-soap \
        --with-libxml-dir \
        --enable-pcntl \
        --enable-shmop \
        --enable-sysvsem \
        --enable-sockets \
        --with-curl \
        --with-zlib \
        --enable-zip \
        --with-bz2 \
        --without-sqlite3 \
        --without-pdo-sqlite \
        --with-pear \
        --with-apxs2=/usr/local/apache/bin/apxs \
        --with-readline \
        --with-config-file-path=/etc \
        --with-config-file-scan-dir=/etc/php.d \
        --with-gd \
        --with-png-dir=/usr \
        --with-jpeg-dir=/usr/lib \
        --enable-gd-native-ttf \
        --with-freetype-dir=/usr \
    && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf phpredis.tar.gz    && cd phpredis    && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf swoole-src.tar.gz  && cd swoole-src  && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php/ && tar xzvf zendopcache.tar.gz && cd zendopcache && phpize && ./configure && make -j$(nproc) && make install',
    'cp -rf /usr/local/src/apache_php/httpd.conf /usr/local/apache/conf',
    'cp -rf /usr/local/src/apache_php/{httpd-vhosts.conf,httpd-mpm.conf} /usr/local/apache/conf/extra/',
    'cp -rf /usr/local/src/apache_php/php.ini /etc/',
 
    
]

path = {
        'src_path':'./service_src_packge/apache_php',
        'dst_path':'/usr/local/src'
        }

service_port = 80
