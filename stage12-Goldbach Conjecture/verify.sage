"""
#the slow algorithm to give glod(n): min non-negative integer make both `n-g` and `n+g` are primes
def gold(n):
    g=0
    while not((is_prime(n-g) and is_prime(n+g))):
        g+=1
    return g
"""

# return (g,step) 
#g:the min non-negative integer make both `n-g` and `n+g` are primes
#step: the count of calling next_prime
def xgold(n):
    g,step=0,0
    p,q=n,n
    while not is_prime(p):
        step+=1
        q=next_prime(q)
        g=q-n
        p=n-g
    return (g,step)


# verify Improved Goldbach's Conjecture
n=344
g,step=xgold(n)
print(n,xgold(n),prime_pi(n))

n=57989356
g,step=xgold(n)
peak=g
print(n,xgold(n),prime_pi(n))

n=198864733
g,step=xgold(n)

while 1:
    if(g>=peak):
        peak=g
        print(n,(g,step))
    elif(g>2000):
        print('  ',n,(g,step))

    n+=1
    g,step=xgold(n)