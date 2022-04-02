# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:15:35 2022

@author: Lenovo
"""
s=input()
import re
pattern=re.compile('<.+?>')
ans=pattern.findall(s)
print(ans)