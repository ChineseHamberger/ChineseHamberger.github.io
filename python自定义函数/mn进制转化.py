# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:42:47 2022

@author: Lenovo
"""
#%%
m,n=map(int,input().split())
num=input()
def cal(num,m):
    dict='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans=0
    for i in range(len(num)):
        ans+=dict.index(num[i])*m**(len(num)-1-i)
    return ans
def con(num,n):
    
    dict='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num<n:
        return dict[num]
    else:
        return con(num//n,n)+dict[num%n]
print(con(cal(num,m),n))
#%%
#优化
m,n=[int(x) for x in input().split()]#m,n可以用列表对应赋值
k=input()
chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def nbase_int(k,n):
    if len(k)==1:
        return chars.index(k)
    else:
        return nbase_int(k[:-1], n)*n+chars.index(k[-1])
def int_nbase(k,n):
    if k<n:
        return chars[k]
    else:
        return int_nbase(k//n, n)+chars[k%n]
print(int_nbase(nbase_int(k,m), n))
    