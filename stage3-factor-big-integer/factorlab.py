from playmath import gcd,sqrt,squareQ

def factor_with_square(n,s=4):
    root=sqrt(n)
    g1,g2=1,1
    while True:
        t=s*s%n
        #print(s,t)
        if s>root:
            flag,rt=squareQ(t)
            if flag:
                g1,g2=gcd(s-rt,n),gcd(s+rt,n)
                print("g1=",g1,"g2=",g2,n%g1)
                break
        #s=t-2
    return (g1,g2)