#! /usr/bin/env python
# coding: utf-8

import threading
import time


class Custom_Thread(threading.Thread):
    def __init__(self, func, args):
        super(Custom_Thread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(self.args)

        
def parallel_thread(thread_list):
    #for _ in thread_list:
    #    _.setDaemon(True)
     
    for _ in thread_list:
        _.start()
    
    for _ in thread_list:
        _.join()

def serial_thread(thread_list):
    for _ in thread_list:
        _.start()
        _.join()



def foo((num1, num2)):
    print num1 + num2
    time.sleep(1)


def foo2((num1, num2)):
    print num1 - num2
    time.sleep(2)
    

if __name__ == '__main__':
    begin=time.time()
    threads=[Custom_Thread(foo,(0,1)), Custom_Thread(foo2,(9,7))]
    serial_thread(threads)
    end=time.time()
    print("serial_thread:All running time is: %s" % (end - begin))

    threads2=[Custom_Thread(foo,(-1,2)), Custom_Thread(foo2,(5,3))]
    parallel_thread(threads2)
    end2 = time.time()
    
    print("parallel_thread:All running time is: %s" % (end2 - end))

    
