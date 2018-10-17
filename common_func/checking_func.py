#! /usr/bin/env python
# coding: utf-8

import socket
import time
from out_color import *

def check_service((ip,port)):
    string = '\n  checking whether the server {0} is using the {1} port'.format(ip, port)
    print '{0} {1}'.format(illustrate_color(string), dot_color('...'))
    time.sleep(1)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        result = sock.connect((ip,int(port)))
        sock.close()
        string = '\n    the service is running or port {0} is occuping in the server {1}\n'.format(port, ip)
        print '{}'.format(progress_color(string))
        return ip
    except:
        pass
        string = '\n     service is not running on the remote server {0} !'.format(ip)
        print '{0}'.format(error_color(string))
        return False
    time.sleep(1)
