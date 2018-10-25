#! /usr/bin/env python
# coding: utf-8

hosts = [
    ['192.168.1.176',22,'root','auqf'],
    ['192.168.1.189',22,'root','auqf']
    ]

service = [
    'yum install -y libtool texinfo redhat-lsb httpd libxcb unzip > /dev/null 2>&1',
    'rm -rf /home/eks && mv /home/eks_wangba /home/eks',
    'cd /home/eks;chmod a+x {chiji_dashen,chiji1,chiji2,ffmpeg,clip,lightpush,lightpush.service,clip.service}',
    'cd /home/eks && mv -f httpd.conf /etc/httpd/conf/',
    'tar xzvf /home/eks/eks_web.tar.gz -C /var/www/html && rm -rf /home/eks/eks_web.tar.gz',
    'cd /home/eks && mv -f {clip,lightpush} /usr/bin/',
    'cd /home/eks && mv -f {libopencv_imgcodecs.so.3.0,libopencv_calib3d.so.3.0,libopencv_imgproc.so.3.0,libopencv_core.so.3.0} /lib64 && ldconfig',
    'cd /home/eks;unzip -o SRS.zip;chmod a+x SRS-CentOS6-x86_64-2.0.243/INSTALL && ./SRS-CentOS6-x86_64-2.0.243/INSTALL &&chmod a+x /usr/local/srs/{etc/init.d,objs}/srs;rm -rf SRS*',
    'cd /home/eks;rpm -ivh gcc-5.4.0-1.el6.x86_64.rpm',
    'echo export PATH=/opt/gcc-5.4.0/bin:\$PATH >> /etc/profile',
    'echo export LD_LIBRARY_PATH=/opt/gcc-5.4.0/lib64/:\$LD_LIBRARY_PATH >> /etc/profile',
    'cd /home/eks && rpm -Uvh glibc*.rpm > /dev/null 2>&1;rm -rf ./*.rpm',
    'cd /home/eks && mv -f {lightpush.service,clip.service} /etc/init.d',
    'iptables -I INPUT -p tcp -m multiport --dports 80,8080,1935,1985 -j ACCEPT',
    'setenforce 0 && /etc/init.d/httpd start && sed -i "s#=enforcing#=permissive#g" /etc/selinux/config',
    '/etc/init.d/srs start',
    '/etc/init.d/lightpush.service start',
    '/etc/init.d/clip.service start',
    '/etc/init.d/iptables save',
    'chkconfig lightpush.service on',
    'chkconfig clip.service on',
    'chkconfig srs on',
    'chkconfig httpd on'
]

path = {
        'src_path':'./service_src_packge/eks_wangba',
        'dst_path':'/home'
        }

service_port = 1935
