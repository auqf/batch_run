#! /usr/bin/env python
# coding: utf-8


def illustrate_color(string):
    return '\033[0;33;40m{0}\033[0m'.format(string)

def dot_color(string):
    return '\033[5;32;40m {0}\033[0m'.format(string)

def progress_color(string):
    return '\033[1;32;40m{0}\033[0m'.format(string)

def push_color(string):
    return '\033[1;34;40m{0}\033[0m'.format(string)
    
def error_color(string):
    return '\033[1;31;40m{0}\033[0m'.format(string)

    
