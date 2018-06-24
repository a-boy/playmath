from factorlab import factor_with_square,gcdFactor
p=1277
b=2*p
n=2**p-1
print(p,n)
#g1,g2=factor_with_square(n,s=p*(p-1))
g=gcdFactor(n,s=p*2,aug=2*p*(p-1)+1,start=1)
print("factored:",g)
