#! /usr/bin/env python
# coding: utf-8

import os
import datetime
from common_func.install_func import serial_install, paralle_install
from common_func.out_color import *


def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".pyc"):
                os.remove(os.path.join(root, name))
    print ("Clear tmp File: " + os.path.join(root, name))

def menu():
    print '''{0}
            1.install srs service
            2.install eks_wangba service
            3.install eks_internet service
            4.test paralle_install
            5.quit
    '''.format(push_color('Service Menu:'))
    choice=input('{}'.format(illustrate_color('Please input your choice: ')))
    return choice

if __name__ == "__main__":
    choice = menu()
    if choice == 1:
        from config.srs_config import *
    elif choice == 2:
        from config.eks_wangba_config import *
    elif choice == 3:
        from config.eks_internet_config import *
    elif choice == 4:
        from config.test_config import *
    elif choice == 5:
        del_files('./')
        exit()
    else:
        print '{0}'.format(illustrate_color('Please input the right number.'))

    starttime = datetime.datetime.now()
    #serial_install(hosts, service, path, service_port)
    paralle_install(hosts, service, path, service_port)
    '''
    if hosts.__len__() > 1:
        paralle_install(hosts, service, path, service_port)
    else:
        serial_install(hosts, service, path, service_port)
    '''
    endtime = datetime.datetime.now()
    del_files('./')
    print 'cost_time: {}s'.format((endtime - starttime).seconds)
