#! /usr/bin/env python
# coding: utf-8

import time
from common_func.thread_func import parallel_thread, serial_thread
from common_func.exec_func import remote_exec
from common_func.checking_func import check_service
from common_func.out_color import *
from thread_func import Custom_Thread

#def install_service(hosts, service, path, service_port):
#    for host_info in hosts:
#        result = check_service(host_info[0],service_port)
#        if result:
#            hosts.remove(host_info)
#    
#    for host_info in hosts:
#        string='\n   try to install the service on the server {}'.format(host_info[0])
#        print '{0}{1}'.format(illustrate_color(string),dot_color('...'))
#        str = '\n     starting upload file to the server {0}'.format(host_info[0])
#        print '{0}{1}'.format(progress_color(str),dot_color('...'))
#        thread_install = remote_exec(host_info, service, path['src_path'],path['dst_path'])
#        for _ in thread_install:
#            serial_thread(_)
#        

#def serial_install(hosts, service, path, service_port):
#    for host_info in hosts:
#        result = check_service((host_info[0],service_port))
#        if result:
#            hosts.remove(host_info)
#
#    for host_info in hosts:
#        string='\n   try to install the service on the server {}'.format(host_info[0])
#        print '{0}{1}'.format(illustrate_color(string),dot_color('...'))
#        str = '\n     starting upload file to the server {0}'.format(host_info[0])
#        print '{0}{1}'.format(progress_color(str),dot_color('...'))
#        remote_exec((host_info, service, path['src_path'],path['dst_path']))

def serial_install(hosts, service, path, service_port):
    check_thread = []
    install_thread = []
    for host_info in hosts:
        check_thread.append(Custom_Thread(check_service,(host_info[0],service_port)))
        
    serial_thread(check_thread)
    
    for _ in check_thread:
        for host_info in hosts:
            if host_info[0] == _.result:
                hosts.remove(host_info)
    for host_info in hosts:
        install_thread.append(Custom_Thread(remote_exec,(host_info, service, path['src_path'],path['dst_path'])))
    
    serial_thread(install_thread)


def paralle_install(hosts, service, path, service_port):
    check_thread = []
    install_thread = []
    
    for host_info in hosts:
        check_thread.append(Custom_Thread(check_service,(host_info[0],service_port)))

    parallel_thread(check_thread)
    
    for _ in check_thread:
        for host_info in hosts:
            if host_info[0] == _.result:
                hosts.remove(host_info)

    for host_info in hosts:
        install_thread.append(Custom_Thread(remote_exec,(host_info, service, path['src_path'],path['dst_path'])))

    parallel_thread(install_thread)
