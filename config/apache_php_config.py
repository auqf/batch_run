#! /usr/bin/env python
# coding: utf-8

hosts = [
     ['59.46.15.211',22,'root','syszy@123']
    ]

service = [
    'yum install -y gcc gcc-c++ libjpeg-devel freetype-devel readline-devel libpng-devel libcurl-devel bzip2-devel openssl-devel libxml2-devel libtool-ltdl-devel  expat-devel bison',
    'ln -s /usr/lib64/libjpeg.so /usr/lib/libjpeg.so',
    'ln -s /usr/lib64/libpng.so /usr/lib/libpng.so',
    'groupadd apache && useradd -g apache -s /sbin/nologin -M apache',
    'cd /usr/local/src/apache_php_package/ && tar xzvf pcre.tar.gz     &&  cd pcre     && ./configure  --prefix=/usr/local/pcre --libdir=/usr/lib64  && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf apr.tar.gz      &&  cd apr      && ./configure  --prefix=/usr/local/apr  --libdir=/usr/lib64  && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf apr-util.tar.gz &&  cd apr-util && ./configure  --with-apr=/usr/local/apr --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf httpd.tar.gz    &&  cd httpd    && ./configure --prefix=/usr/local/apache \
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
    'cd /usr/local/src/apache_php_package/ && tar xzvf libmcrypt.tar.gz && cd libmcrypt && ./configure  --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf mhash.tar.gz     && cd mhash     && ./configure  --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf mcrypt.tar.gz    && cd mcrypt    && ./configure  --libdir=/usr/lib64 && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf php-src.tar.gz   && cd php-src   && ./buildconf --force && ./configure \
        --with-gd \
        --with-bz2 \
        --with-curl \
        --with-zlib \
        --with-pear \
        --enable-zip \
        --with-iconv \
        --with-mhash \
        --with-mcrypt \
        --enable-soap \
        --with-gettext \
        --enable-pcntl \
        --enable-shmop \
        --with-openssl \
        --enable-bcmath \
        --with-readline \
        --disable-debug \
        --disable-rpath \
        --enable-shared \
        --enable-opcache \
        --enable-sysvsem \
        --enable-sockets \
        --enable-mbstring \
        --with-libxml-dir \
        --without-sqlite3 \
        --with-png-dir=/usr \
        --without-pdo-sqlite \
        --with-mysql=mysqlnd \
        --with-mysqli=mysqlnd \
        --enable-gd-native-ttf \
        --with-pdo-mysql=mysqlnd \
        --with-freetype-dir=/usr \
        --with-jpeg-dir=/usr/lib \
        --with-config-file-path=/etc \
        --enable-inline-optimization \
        --with-config-file-scan-dir=/etc/php.d \
        --with-apxs2=/usr/local/apache/bin/apxs \
    && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf phpredis.tar.gz    && cd phpredis    && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf swoole-src.tar.gz  && cd swoole-src  && phpize && ./configure && make -j$(nproc) && make install',
    'cd /usr/local/src/apache_php_package/ && tar xzvf zendopcache.tar.gz && cd zendopcache && phpize && ./configure && make -j$(nproc) && make install',
    '\cp -rf /usr/local/src/apache_php_package/php.ini /etc/',
    '\cp -rf /usr/local/src/apache_php_package/httpd.conf /usr/local/apache/conf',
    '\cp -rf /usr/local/src/apache_php_package/{httpd-vhosts.conf,httpd-mpm.conf} /usr/local/apache/conf/extra/'
    
]

path = {
        'src_path':'./service_src_packge/apache_php_package',
        'dst_path':'/usr/local/src'
        }

#service_port = 80
