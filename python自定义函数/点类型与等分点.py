# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 22:30:02 2022

@author: Lenovo
"""

points={'left':(-200,-200),
        'topl':(-200,200),
        'topr':(200,200),
        'right':(200,-200)}
#四个点的集合
points=dict(left=(-200,-200),
            right=(200,-200),
            topl=(-200,200),
            topr=(200,-200))
#更快的创建

#点函数
def get3_1(p1,p2):
    return ((2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3)
def get3_2(p1,p2):
    return ((p1[0]+p2[0]*2)/3,(p1[1]+p2[1]*2)/3)
def move(p,right,up):
    return (p[0]+right,p[1]+up)
#批量创建
namelist=['left','right','topl','topr']
plist=[(-200,-200),(200,-200),(-200,200),(200,-200)]

def create_points(namelist,plist):
    return dict(zip(namelist,plist))
points=create_points(namelist,plist)

def move_points(points,right,up):
    nl=[]
    pl=[]
    for item in list(points.items()):
        nl.append(item[0])
        pl.append(move(item[1],right,up))
    return dict(zip(nl,pl))

print(move_points(points, 3, 5))


        
    
#点的转化
points={'left':get3_1(points['topl'],points['right']),
               'right':get3_1(points['topr'],points['left']),
               'topl':get3_1(points['topl'],points['topr']),
               'topr':get3_1(points['topr'],points['topl'])}




        