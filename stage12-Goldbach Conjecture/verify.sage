def gold(n):
    for g in range(0,prime_pi(n)+2):
        if (is_prime(n-g) and is_prime(n+g)):
            return g

# check Improved Goldbach's Conjecture
n=344
print(n,gold(n),prime_pi(n))
n=1259168
while gold(n)>=0:
    print(n)
    n+=1