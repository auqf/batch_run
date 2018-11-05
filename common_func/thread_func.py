#! /usr/bin/env python
# coding: utf-8

import threading
import time


class Custom_Thread(threading.Thread):
    def __init__(self, func, args):
        super(Custom_Thread, self).__init__()
        self.func = func
        self.args = args
        

    def run(self):
        try:
            self.result = self.func(self.args)
        except Exception, e:
            print e
            exit()

        
def parallel_thread(thread_list):
    for _ in thread_list:
        _.start()
    
    for _ in thread_list:
       if _.isAlive():
        _.join()

def serial_thread(thread_list):
    for _ in thread_list:
        _.start()
        if _.isAlive():
            _.join()


mutex = threading.Lock()
def foo((num1, num2)):
    print num1 + num2
    time.sleep(1)
    


def foo2((num1, num2)):
    mutex.acquire()
    print num1 - num2
    time.sleep(2)
    mutex.release()
    

if __name__ == '__main__':
    begin=time.time()
    threads=[Custom_Thread(foo,(0,1)), Custom_Thread(foo2,(9,7))]
    serial_thread(threads)
    end=time.time()
    print("serial_thread:All running time is: %s" % (end - begin))

    threads2=[Custom_Thread(foo2,(5,3)), Custom_Thread(foo2,(9,7)),Custom_Thread(foo2,(6,4))]
    parallel_thread(threads2)
    end2 = time.time()
    
    print("parallel_thread:All running time is: %s" % (end2 - end))

    
