from factorlab import factor_with_square
p=1277
b=2*p
n=2**p-1
print(p,n)
g1,g2=factor_with_square(n,s=p*(p-1))
print("factored:",g1,g2)
