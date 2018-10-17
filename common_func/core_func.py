#! /usr/bin/env python
# coding:utf-8

import os
import sys
import math
import time
import paramiko
from out_color import *



class SSHConnection(object):
    def __init__(self,ip,port,username,pwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.pwd = pwd
        self.transport = paramiko.Transport((ip, port))
        self.transport.connect(username=username, password=pwd)
        self.ssh = paramiko.SSHClient()
        self.ssh._transport = self.transport
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        
    def progress_bar(self, num_cur):
        rows, columns = os.popen('stty size', 'r').read().split()
        ratio = float(num_cur / 100.0)
        if int(columns) > 33:
            percentage = int(ratio * (int(columns)-21))
            r = '       [%s%s]%d%%\n\r' % (">"*percentage, " "*(int(columns)-percentage-21), ratio*100)
        else:
            percentage = int(ratio * 100)
            r = '       [%s%s]%d%%\n\r' % (">"*percentage, " "*(100 - percentage), percentage)
        sys.stdout.write(illustrate_color(r))
        sys.stdout.flush()
        
    #def connect(self):
    #    #paramiko.util.log_to_file('paramiko_login_log') 
    #    self.transport = paramiko.Transport((self.ip,self.port))
    #    self.transport.connect(username=self.username,password=self.pwd)
    #    self.ssh = paramiko.SSHClient()
    #    self.ssh._transport = self.transport
    #    self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        

    def cmd(self,command):
        string='\n     starting install the service on the server {}'.format(self.ip)
        print '{0}{1}'.format(progress_color(string),dot_color('...'))
        total_=command.__len__()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        num, dot = str(100.0/total_).split('.')
        dot = (100 - int(num)*total_)/float(total_)
        base_ = int(num) + int(dot)
        cur_ = base_
        for _ in command:
            stdin, stdout, stderr = self.ssh.exec_command(_)
            result = stderr.readlines()
            if len(result) > 0 and sum([item.count('is already installed') for item in result]) == 0:
                string = '         Error:"{0}"\n         {1}         break install at \033[5;33;40m========> \033[0m{2}%'.format(_, '         '.join(result), int(cur_))
                print error_color(string)
                string = '         service install failed, disconnect the connection of the server {}\n\n'.format(self.ip)
                print error_color(string)
                break
            if command.index(_)  == total_ - 1:
                self.progress_bar(100)
            else:
                self.progress_bar(cur_)
                cur_ += base_

    def upload(self, src_path, dst_path, tag=1):
        if tag == 1:
            name = src_path.split('/')[-1]
            dst_root = os.path.join(dst_path, name)
        else:
            dst_root = dst_path

        if os.path.isfile(src_path):
            try:
                self.sftp.put(src_path, os.path.join(dst_root))
                str = "       upload {0}{1}{2}'s {3} successfully".format(push_color(src_path), dot_color(':::>'), self.ip, push_color(os.path.join(dst_root)))
                print(str)
            except Exception,e:
                pass
        else:
            try:
                self.sftp.stat(dst_root)
            except Exception,e:
                try:
                    self.sftp.mkdir(dst_root)
                except Exception, e:
                    pass
            files = os.listdir(src_path)
            for f in files:
                tag += 1
                src = os.path.join(src_path, f)
                dst = os.path.join(dst_root, f)
                self.upload(src, dst, tag)


    def close(self):
        self.transport.close()
