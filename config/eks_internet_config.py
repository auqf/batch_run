#! /usr/bin/env python
# coding: utf-8

hosts = [['124.115.159.83',22,'root','ems.1234']
    ]

service = [
    'rpm -ivh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm',
    'yum install -y libtool texinfo redhat-lsb httpd libxcb unzip sshpass> /dev/null 2>&1',
    'rm -rf /home/eks && mv /home/eks_internet /home/eks',
    'cd /home/eks;chmod a+x {chiji_dashen,chiji1,chiji2,ffmpeg,clip,clip.service,do_video.service,ffmpeg_ingest}',
    'cd /home/eks && mv -b httpd.conf /etc/httpd/conf/',
    'tar xzvf /home/eks/eks_web.tar.gz -C /var/www/html && rm -rf /home/eks/eks_web.tar.gz',
    'cd /home/eks && mv -f {clip,ffmpeg_ingest} /usr/bin/',
    'cd /home/eks && mv -f {libopencv_imgcodecs.so.3.0,libopencv_calib3d.so.3.0,libopencv_imgproc.so.3.0,libopencv_core.so.3.0} /lib64 && ldconfig',
    'cd /home/eks;unzip -o SRS.zip;chmod a+x SRS-CentOS6-x86_64-2.0.243/INSTALL && ./SRS-CentOS6-x86_64-2.0.243/INSTALL && chmod a+x /usr/local/srs/{etc/init.d,objs}/srs;rm -rf SRS*',
    'cd /home/eks;rpm -ivh gcc-5.4.0-1.el6.x86_64.rpm',
    'echo export "PATH=/opt/gcc-5.4.0/bin:\$PATH" >> /etc/profile',
    'echo export "LD_LIBRARY_PATH=/opt/gcc-5.4.0/lib64/:\$LD_LIBRARY_PATH" >> /etc/profile',
    'cd /home/eks && rpm -Uvh glibc*.rpm > /dev/null 2>&1;rm -rf ./*.rpm',
    'cd /home/eks && mv -f {clip.service,do_video.service} /etc/init.d',
    'iptables -I INPUT -p tcp -m multiport --dports 80,8088,8080,1935,1985 -j ACCEPT',
    'setenforce 0 && /etc/init.d/httpd start && sed -i "s#=enforcing#=permissive#g" /etc/selinux/config',
    'echo "sh /etc/init.d/do_video.service" >> /etc/rc.local',
    '/etc/init.d/clip.service start',
    '/etc/init.d/srs start',
    '/etc/init.d/iptables save',
    'chkconfig clip.service on',
    'chkconfig srs on',
    'chkconfig httpd on',
    'echo "\n" | sh /etc/init.d/do_video.service &',
    'echo "\n" | sh /home/eks/run.sh &'
]

path = {
        'src_path':'./service_src_packge/eks_internet',
        'dst_path':'/home'
        }

service_port = 1935
