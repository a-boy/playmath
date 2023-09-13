def hpf_seq(top):
   H=[0,1,2,3]
   for n in range(4,top):
        prime_factors=[part[0] for part in list(factor(n))]
        cursor=-1
        while len(prime_factors)>1:
            if H[cursor] in prime_factors:
                prime_factors.remove(H[cursor])
            cursor-=1
        hpf=prime_factors[0]
        H.append(hpf)
   return H
i=1
for h in  hpf_seq(40000)[1:]:
    print(i,h)
    i+=1