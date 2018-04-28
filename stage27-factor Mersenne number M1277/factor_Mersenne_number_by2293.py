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
    if x == 0:
        return (True,0)
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

def factorMersenne(p,klow=1): 
    b=2*p
    M=(1<<p)-1
    K=(M-1)//b
    print(p,b,M,K)
    # b*k1*k2+k1+k2=K
    #c=k1+k2
    high=(square_Newton(1+b*K)-1)//b
    print('klow=',klow,'high=',high)
    k1=high
    re=1
    while(re!=0):
        se=re%k1
        k1-=(3+se)%k1>>2
        #print (re,se,k1)
        if k1<klow or se==0:
            high=high-1
            k1=high
        re=(K-k1)%(b*k1+1)
        
       # print(flag,delta,c)
        
    k2=(K-k1)//(b*k1+1)
    print(k1,k2,b)
    q1,q2=b*k1+1,b*k2+1
    print(q1,q2)
    print(q1*q2-M==0)
    

factorMersenne(1277,2**65//2554)
