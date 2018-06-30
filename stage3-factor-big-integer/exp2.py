from factorlab import factor_with_square_4ksub1,gcdFactor
p=1277
b=2*p
n=2**p-1
print(p,n)
g=factor_with_square_4ksub1(n)

print("factored:",g)
