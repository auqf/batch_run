#! /usr/bin/env python
# coding: utf-8

import os
import datetime
from common_func.install_func import install, exec_command
from common_func.out_color import *


def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".pyc"):
                os.remove(os.path.join(root, name))
    print ("Clear tmp File: " + os.path.join(root, name))

def menu():
    print '''{0}
            0.init server
            1.remote_exec_command           2.install srs service         3.install eks_wangba service
            4.install eks_internet service  5.install vsftp service       6.install Atlas service
            7.intall mysql-8.0 service      8.install nginx lua service   9.install nginx php service
            10.install apache php service   11.install redis service
            12.quit
    '''.format(push_color('Service Menu:'))
    choice=input('{0}'.format(illustrate_color('Please input your choice: ')))
    return choice

if __name__ == "__main__":
    choice = menu()
    if choice == 1:
        from config.init_server_config import *
    elif choice == 1:
        from config.remote_cmd_config import *
    elif choice == 2:
        from config.srs_config import *
    elif choice == 3:
        from config.eks_wangba_config import *
    elif choice == 4:
        from config.eks_internet_config import *
    elif choice == 5:
        from config.vsftp_config import *
    elif choice == 6:
        from config.atlas_config import *
    elif choice == 7:
        from config.mysql_config import *
    elif choice == 8:
        from config.nginx_lua_config import *
    elif choice == 9:
        from config.nginx_php_config import *
    elif choice == 10:
        from config.apache_php_config import *
    elif choice == 11:
        from config.redis_config import *
    elif choice == 12:
        del_files('./')
        exit()
    else:
        print '{0}'.format(illustrate_color('Please input the right number.'))

    starttime = datetime.datetime.now()
    arg=raw_input('{0}'.format(illustrate_color('\nPlease select your install_method, s or p: ')))
    if arg not in ['s', 'p']:
        print '{0}'.format(error_color('Please input the right method.'))
        exit()
    
    if  vars().has_key('service_port'):
        install(hosts, service, path, service_port, arg)
    else:
        exec_command(hosts, service, arg)
    
    endtime = datetime.datetime.now()
    del_files('./')
    print 'cost_time: {0}s'.format((endtime - starttime).seconds)
