# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 19:17:41 2022

@author: Lenovo
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
prec={}#precedence优先级
prec['^']=4
prec['*']=3
prec['/']=3
prec['+']=2
prec['-']=2
prec['(']=1    
def math(op,s1,s2):
    if op=='*':
        return s1*s2
    if op=='/':
        return s1/s2
    if op=='+':
        return s1+s2
    if op=='-':
        return s1-s2
    if op=='^':
        return s1**s2
    

def calculate(s) -> float:    
    op_stack=Stack()
    num_stack=Stack()
    token_stack=s.split()
    #print(token_stack,'token')
    for token in token_stack:       
        if token.isdigit():   
            num_stack.push(token)
            
        elif token=='(':
            op_stack.push(token)
         
        elif token==')':
            top=op_stack.pop()
            
            while top!='(':           
                s2=int(num_stack.pop())
                s1=int(num_stack.pop())
                num_stack.push(math(top,s1,s2))
                
                top=op_stack.pop()
             
        else:
            while not op_stack.isEmpty() and prec[op_stack.peek()]>=prec[token]:
             
                op=op_stack.pop()
                s2=int(num_stack.pop())
                s1=int(num_stack.pop())
                num_stack.push(math(op,s1,s2))
                
            op_stack.push(token)
            #print(op_stack,'op')
    while not op_stack.isEmpty():
        op=op_stack.pop()
        s2=int(num_stack.pop())
        s1=int(num_stack.pop())
        num_stack.push(math(op,s1,s2))    
    return num_stack.items[0]
    

# 调用检验

print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))