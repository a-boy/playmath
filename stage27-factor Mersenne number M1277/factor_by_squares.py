# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:12:25 2018

@author: ljl
"""
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def squareQ(x):
    if x == 1:
        return (True,1)
    low = 0
    high = x // 2
    root = high
    while root * root != x:
       root = (low + high) // 2
       if low + 1 >= high:
          return (False,low)
       if root * root > x:
          high = root
       else:
          low = root
    return (True,root)

def is_square(x):
    if x == 1:
        return True
    low = 0
    high = x // 2
    root = high
    while root * root != x:
       root = (low + high) // 2
       if low + 1 >= high:
         # print('floor(sqrt(x))=',low)
          return False
       if root * root > x:
          high = root
       else:
          low = root
    #print (root)
    return True    
def square_Newton(n):
    if n == 1:
        return True
    r = n//2
    s=2
    while s!=r:
        r=s
        s= (r+n//r)>>1
      
    return r

def factor(n): 
    s=513
    i=1     
    while(True):
        t=s*s%M    
        i+=1
       # print(i,'s=',s,'t=',t)
            
        if(is_square(t) and t!=s*s):
            print('factored')
            print(i,'prev=',s,'t=',t)
            root=square_Newton(t)
            g1= gcd(s+root,M)
            g2= gcd(s-root,M)
            print('gcd:',g1,g2)
            break
        s=t-2
    

p=1277
M=2**p-1
print(M)
factor(M)
