from playmath import gcd,sqrt,squareQ

def factor_with_square_4ksub1(n,s=4):
    flag,r=squareQ(n)
    g=1
    while not flag:
        while(r%2==0):
            r=r//2
        s=r
        t=s*s%n +n
        flag,r=squareQ(t)
        print(s,r)

        #s=t-2
    g=gcd(s-r,n)
    print("factored!g=",g,n%g)
    return g

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

def factor_by_ahmeng(n,init=0):
    x,y=init,-1
    if init==0: x,y=5,sqrt(n)
    while x!=y:
        x=y
        y=x*x%n-x-3
        print(x,y)
    g1,g2=gcd(n,x-3),gcd(n,x+1)
    print('g1=',g1,'g2=',g2)
    return g1

def factor_by_ahmeng4(n):
    x,y=17,(n+1)>>1
    while x!=y and y>0:
        x=y
        r=(x*(x-1))%n
        y=r+1-4
        print(y,r)
    g1,g2=gcd(n,x+1),gcd(n,x-3)
    print('g1=',g1,'g2=',g2)
    return g1

def factor_by_ahmeng5(n):
    c,x=(n+3)>>1,(n+1)>>1
    while t!=x:
        t=x
        x=(x*x-c+2)%n
        c=2+n-x
        print(x)
    g1,g2=gcd(n,x+2),gcd(n,x-2)
    print('g1=',g1,'g2=',g2)
    return g1