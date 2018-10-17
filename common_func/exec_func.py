#! /usr/bin/env python
# coding: utf-8

from common_func.core_func import SSHConnection


#def remote_exec(host_info,service,src_path,dst_path):
#    thread_connect = []
#    thread_upload = []
#    thread_command = []
#    thread_close = []
#    ip = host_info[0]
#    port = host_info[1]
#    username = host_info[2]
#    password = host_info[3]
#    ssh = SSHConnection(ip,port,username,password)
#    #thread_connect.append(threading.Thread(target=ssh.connect))
#    thread_upload.append(threading.Thread(target=ssh.upload, args=(src_path,dst_path,)))
#    thread_command.append(threading.Thread(target=ssh.cmd, args=(service,)))
#    thread_close.append(threading.Thread(target=ssh.close))
#    #return [thread_connect, thread_upload, thread_command, thread_close]
#    return [thread_upload, thread_command, thread_close]
def remote_exec((host_info,service,src_path,dst_path)):
    ip = host_info[0]
    port = host_info[1]
    username = host_info[2]
    password = host_info[3]
    try:
        remote_ssh = SSHConnection(ip,port,username,password)
        remote_ssh.upload(src_path, dst_path)
        remote_ssh.cmd(service)
        remote_ssh.close()
    except Exception, e:
        raise e

def local_exec(func, args):
    pass
    #print '\033[1;32;40mSRS sevice  is not running on the remote server {0} !\033[0m'.format(host_info[0])
    #thread_check = []
    #thread_check.append(threading.Thread(target=func, args=(args,)))
    #return [thread_check]
