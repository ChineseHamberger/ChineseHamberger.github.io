# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:08:12 2022

@author: Lenovo
"""

import time
from functools import wraps
def fn_timer(function):
    @wraps(function)
    def function_timer(*args,**kwargs):
        t0=time.time()
        result=function(*args,**kwargs)
        t1=time.time()
        print('总共运行时间为{}秒'.format(str(t1-t0)))
        return result
    return function_timer
@fn_timer
def f():
    pass
f()