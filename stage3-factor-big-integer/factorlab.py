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
    return g1

def gcdFactor(n,s=1024,aug=2293,start=1):
    block=(n-start)//s
    x=start
    g=1;i=0
    while i<s:
        j=0
        print('x',i,j)
        while j<aug:
            g=gcd(n,x)
            if(g>1):
                print("factored!g=",g,n%g,'i,j=',i,j)
                return g
            x+=1;j+=1
        x+=block;i+=1
    print('g==1 for n when s=',s,aug,start)
    return 1