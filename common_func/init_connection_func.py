#! /usr/bin/env python
# coding: utf-8

from common_func.core_func import SSHConnection
from common_func.out_color import *


def remote_install((host_info,service,src_path,dst_path)):
    ip = host_info[0]
    port = host_info[1]
    username = host_info[2]
    password = host_info[3]
    try:
        remote_ssh = SSHConnection(ip,port,username,password)
        string = '\n  starting upload install files to the server {0} !'.format(ip)
        print '{0}'.format(illustrate_color(string))
        remote_ssh.upload(src_path, dst_path)
        remote_ssh.cmd(service)
        remote_ssh.close()
    except Exception, e:
        raise e

def local_exec((host_info,service)):
    ip = host_info[0]
    port = host_info[1]
    username = host_info[2]
    password=host_info[3]
    try:
        remote_ssh = SSHConnection(ip,port,username,password)
        remote_ssh.cmd(service)
        remote_ssh.close()
    except Exception, e:
        raise e