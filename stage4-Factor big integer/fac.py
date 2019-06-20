from math import gcd
def factorWithSquareTriangularNumber(r):
    farv=4096
    ST=[1,36]
    u=[1,6]
    i=1
    ind=-1
    while True:
        i+=1
        st=(34*ST[i-1]%r-ST[i-2]+2) % r
        u.append((6*u[i-1]-u[i-2])%r)
        # if st is a Triangular Numbers or a square or have in ST[],then n is factored
        if st< farv:
            print("small value at i,u[i],ST[i]",i,u[i],st)
        try:
            ind=ST.index(st)
        except ValueError:
            pass

        if ind>=0:
            print("factored! at i,u[i]",i,u[i],"index=",ind)
            q=gcd(u[i]-u[ind],r)
            p=gcd(u[i]+u[ind],r)
            print("p,q=",p,q)
            return (p,q)
        else:
            ST.append(st)