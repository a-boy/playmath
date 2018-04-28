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

def factorMersenne_c(p,c_low=0,k_low=1): 
    b=2*p
    M=(1<<p)-1
    K=(M-1)//b
    print(p,b,M,K)
    # b*k1*k2+k1+k2=K
    #c=k1+k2
    k_high=(K-k_low)//(b*k_low+1)
    c_top=k_low+k_high
    mid=(square_Newton(1+b*K)-1)//b
    print('mid=',mid)
    c=2*mid
    if c_low>c:c=c_low
      
    c+=(K-c)%b # keep (K-c)%b==0

    flag,delta=False,0
    i=0
    while(not flag ):
       flag,delta=squareQ(c*c-2*(K-c)//p)

       i+=1
       if(i>=10000):
         i=0
         print(flag,c,delta)
       
       c+=b
       
    if(flag):
           k1,k2=(c-delta)//2,(c+delta)//2
           print(k1,k2,b)
           q1,q2=b*k1+1, b*k2+1
           print(q1,q2)
           print(q1*q2-M==0)
           return [q1,k1,q2,k2,p,'2^p-1 is composite']
          
    return [1,0,1,0,p,'2^p-1 is prime']
   # k2=(K-k1)//(b*k1+1)


def factorMersenne(p,k_low=1): 
    b=2*p
    M=(1<<p)-1
    K=(M-1)//b
    print('>>> p=',p,b,'M=',M,K)
    # b*k1*k2+k1+k2=K
    #c=k1+k2
    mid=(square_Newton(1+b*K)-1)//b
    
    print('k_low=',k_low,mid)
    k1,k2=mid-1,mid+1
    re=1
    while(k1>k_low):
        k2=(K-k1)//(b*k1+1)
        re=(K-k1)%(b*k1+1)
        print(k2,re)
        if(re==0):
            q1,q2=b*k1+1, b*k2+1
            print(q1,k1,q2,k2,p,"2**p-1 is composite")
            return (q1,k1,q2,k2,p,"2**p-1 is composite")
        else:
            k2+=1
            
        k1=(K-k2)//(b*k2+1)
        re=(K-k2)%(b*k2+1)
        print(k1,re)
        if(re==0):
            q1,q2=b*k1+1, b*k2+1
            print(q1,k1,q2,k2,p,"2**p-1 is composite")
            return (q1,k1,q2,k2,p,"2**p-1 is composite")
        else:
            k1-=1
        
    return (1,k1,1,k2,p,"2**p-1 may prime! no great then 1+2*p*k_low")
    
#print(factorMersenne(37,1))
#print(factorMersenne(41,0))
#print(factorMersenne_c(1277,2**65//2554))
  1263168637228502089917866066041310012536194688969555554280001457629507362240798264339407358964873126432365904298489316102735865645296739441884868855943466804240053880152490599576867119175477
import sys
p=int(sys.argv[1])
low=int(sys.argv[2])
print(factorMersenne_c(p,c_low=low))
