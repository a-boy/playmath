# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:47:21 2018

@author: github.com/a-boy
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

def square_Newton(n):
    if n == 1:
        return True
    r = n//2
    s=2
    while s!=r:
        r=s
        s= (r+n//r)>>1
      
    return r