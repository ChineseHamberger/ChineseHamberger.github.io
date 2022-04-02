# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:10:09 2022

@author: Lenovo
"""

n=int(input())
s=input()
maze=[[s]*n for i in range(n)]
#不能用[[s]*n]*n否则索引有问题
def cut(maze,a,b,c,d):#操作函数
    #从ab位到cd位的矩阵
    if c-a>=2:
        for i in range(a+(c-a+1)//3,a+2*(c-a+1)//3):       
            for j in range(b+(d-b+1)//3,b+2*(d-b+1)//3):            
                maze[i][j]=' '*len(s)
        cut(maze,a,b,a+(c-a+1)//3-1,b+(d-b+1)//3-1)
        cut(maze,a,b+(d-b+1)//3,a+(c-a+1)//3-1,b+2*(d-b+1)//3-1)
        cut(maze,a,b+2*(d-b+1)//3,a+(c-a+1)//3-1,d)   
        cut(maze,a+(c-a+1)//3,b,a+2*(c-a+1)//3-1,b+(d-b+1)//3-1)
        cut(maze,a+(c-a+1)//3,b+2*(d-b+1)//3,a+2*(c-a+1)//3-1,d)
        cut(maze,a+2*(c-a+1)//3,b,c,b+(d-b+1)//3-1)
        cut(maze,a+2*(c-a+1)//3,b+(d-b+1)//3,c,b+2*(d-b+1)//3-1)
        cut(maze,a+2*(c-a+1)//3,b+2*(d-b+1)//3,c,d)            
cut(maze,0,0,n-1,n-1)
for i in range(n):
    print(''.join(maze[i]))