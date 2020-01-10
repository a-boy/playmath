def fib3(i):
    a,b,c=0,1,1
    print(a,b,c)
    while (i>0):
        a=b+c;b=c+a;c=a+b;
        print(a,b,c)
        i-=1

fib3(2293)
