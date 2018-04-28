from sympy import prime as p
from math import ceil,sqrt
i=1
r=1
x,y=p(i),p(i+1)

while i<100000:
    csqrt=ceil(sqrt(i))
    g=y-x
    if g>=csqrt: print(i,g,csqrt)
        
    i+=1
    x,y=y,p(i+1)