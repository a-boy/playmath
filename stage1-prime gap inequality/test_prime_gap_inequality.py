# test  p[i+1]-p[i]<=i
from sympy import prime as p
i=1
x,y=p(i),p(i+1)

while y-x<=i:
    print(i,y-x)
    i+=1
    x,y=y,p(i+1)
    

print(i,y-x)    
