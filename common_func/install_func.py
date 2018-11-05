#! /usr/bin/env python
# coding: utf-8

import time
from common_func.thread_func import parallel_thread, serial_thread
from common_func.init_connection_func import remote_install, local_exec
from common_func.checking_func import check_service
from thread_func import Custom_Thread


def install(hosts, service, path, service_port, arg):
    if arg == "p":
        func = parallel_thread
    else:
        func = serial_thread
    
    check_thread = []
    install_thread = []
    for host_info in hosts:
        check_thread.append(Custom_Thread(check_service,(host_info[0],service_port)))
        
    func(check_thread)
    
    for _ in check_thread:
        for host_info in hosts:
            if host_info[0] == _.result:
                hosts.remove(host_info)
    for host_info in hosts:
        install_thread.append(Custom_Thread(remote_install,(host_info, service, path['src_path'],path['dst_path'])))
    
    func(install_thread)

def exec_command(hosts, service, arg):
    if arg == "p":
        func = parallel_thread
    else:
        func = serial_thread
        
    exec_thread = []
    for host_info in hosts:
        exec_thread.append(Custom_Thread(local_exec,(host_info, service)))
    
    func(exec_thread)