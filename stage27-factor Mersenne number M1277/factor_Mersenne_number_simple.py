# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:17:45 2018

@author: ljl
"""
from playmath import square_Newton
def factorMersenne_simple(p,k_low=0): 
    b=2*p
    M=(1<<p)-1
    K=(M-1)//b
    print('>>> p=',p,b,'M=',M,K)
    # b*k1*k2+k1+k2=K
    #c=k1+k2
    mid=(square_Newton(1+b*K)-1)//b
    
    print('k_low=',k_low,mid)
    k1=mid+4-mid%4
    k2=k1-p%4
    re=1
    while(re!=0 and k1>k_low):
        re=(K-k1)%(b*k1+1)
        if(re==0):
            k2=(K-k1)//(b*k1+1)
            q1,q2=b*k1+1, b*k2+1
            print(q1,k1,q2,k2,p,"2**p-1 is composite")
            return (q1,k1,q2,k2,p,"2**p-1 is composite")
        k1-=4
        
        re=(K-k2)%(b*k2+1)
        if(re==0):
            k1=(K-k2)//(b*k2+1)
            q1,q2=b*k1+1, b*k2+1
            print(q1,k1,q2,k2,p,"2**p-1 is composite")
            return (q1,k1,q2,k2,p,"2**p-1 is composite")
        k2-=4
        
        
    return (1,k1,1,k2,p,"2**p-1 may prime! no great then 1+2*p*k_low")
    
print(factorMersenne_simple(1277,2**64))
#print(factorMersenne(37,1))