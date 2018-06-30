from factorlab import factor_by_ahmeng5,gcdFactor
import sys
p=int(sys.argv[1])
b=2*p
n=2**p-1
print(p,n)
#g1,g2=factor_with_square(n,s=p*(p-1))
g=factor_by_ahmeng5(n)
print("factored:",g)
