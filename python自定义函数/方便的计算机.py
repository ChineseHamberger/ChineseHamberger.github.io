# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:21:06 2022

@author: Lenovo
"""
#%%
#已知通项求和
print('请输入通项公式：（无需输入an=,直接输入含n的表达式)')
str=input()
def an(n):
    return eval(str)
print('请输入项数：')
n=int(input())
s=0
for i in range(1,n+1):
    s+=an(i)
print(s)
#%%
#求方程近似根
def solve(f, x1, x2):
    mid = (x1 + x2) / 2
    if f(mid) == 0 or abs(x1 - x2) < 1e-8:
        return mid
    elif f(mid) * f(x1) > 0:
        return solve(f,mid,x2)
    else:
        return solve(f,x1,mid)
print('请输入所需函数：(含x的表达式）')
str=input()
def f(x):
    return eval(str)
print('请输入预测根的范围：')
a,b=map(float,input().split())
print('二分法求得的结果为',solve(f,a,b))
#%%
#等比数列求和
print('请输入首项，公比，项数：')
a1,q,n=map(float,input().split())
print(a1*(q**n-1)/(q-1))
#%%
#进制转化
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
