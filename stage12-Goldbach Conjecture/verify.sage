def gold(n):
    for g in range(0,prime_pi(n)+2):
        if (is_prime(n-g) and is_prime(n+g)):
            return g

# check Improved Goldbach's Conjecture
n=344
peak=gold(n)
print(n,gold(n),prime_pi(n))

n=2887462
g=gold(n)
while g>=0:
    if(g>1000):
        #peak=g
        print(n,g,prime_pi(n))
    n+=1
    g=gold(n)