def biggcd(a, b):
  while b:
    a, b = b, a % b
    if a<=10000000000: return 1
  return a

def gcdfib(n):
    """
    factor n by computing gcd(n,fibonacci(i)), i in [1..m]
    """
    i,a,b=2,1,1

    print(i,a,b)
    g=1
    while g==1:
        a,b=b,(a+b)%n
        g=biggcd(n,b)
        i+=1
        if(i%10000000==0): print(i,a,b)
    print('g=',g)
    return g

p=1277
n=2^p-1
gcdfib(n)