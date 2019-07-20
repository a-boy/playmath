# playmath
a boy's math playground; math experiment

https://nbviewer.jupyter.org/github/a-boy/playmath/tree/master/

## idea:(mailto:a_boy@live.com)
- Prime-Gap-Inequality: The i-th prime gap `p[i+1]-p[i]<=i` . In other words, `range(n,n+primepi(n)+1)` contains one or more primes. So, the i-th prime `p[i]<=1+2+...+ i-1 + p[1] = i*(i-1)/2 +2`
- Bread curve
- `range(n^2, n*(n+1))` contains at least one prime. This is because: as to the array `{n*n, n*n+1, n*n+2, ... ,nextprime(n*n)-1 }`, we can dispatch distinct real factors for every item, these real factors are in `{2,3,4,...,n}` , Pigeonhole principle shows `nextprime(n*n)< n*(n+1)` . Samely, `range(n*(n+1), (n+1)*(n+1))` contains at least one prime. so, this is one sentence proof for 
    ```
    "still unsolved Legendre's conjecture asks whether for every n > 1, there is a prime p, such that n^2 < p < (n + 1)^2 "

    https://en.wikipedia.org/wiki/Legendre%27s_conjecture
    ```
- Try to prove Goldbach's Conjecture
```
    For any integer n>=2, there exists g=gold(n) , 0=<g<=primepi(n), satisfies that both n-g and n+g are primes. 
    ?? because we can dispatch distinct prime factors for {n+1, n+2, ... n+g}.replace( isprime(n+x) => n-x) ?? 
```

- n>=3, let `p=nextprime(n!)-n!` , then p is always prime or 1, because p is less than ` nextprime(n)^2` , very often ` p<n^2 ` .
Conjecture: for any n>=3, ` n! - prevprime(...(prevprime(n!))) ` is always prime or 1, the count of nest `prevprime` can be from 1 to n-1 times.

- denote S(k,v):=RamseyNumber(k+1,v+1)-1 . 
Conjecture: for any integer v>=2, S(2,v)%5 in {0,2,3}, here S(2,v)=RamseyNumber(3,v+1)-1 . 
RamseyNumber(3,v+1) can NOT be the form 5*k or 5*k+2

```
m	n	R(m,n)	Reference
3	3	6	Greenwood and Gleason 1955
3	4	9	Greenwood and Gleason 1955
3	5	14	Greenwood and Gleason 1955
3	6	18	Graver and Yackel 1968
3	7	23	Kalbfleisch 1966
3	8	28	McKay and Min 1992
3	9	36	Grinstead and Roberts 1982
3	10	[40, 43]	Exoo 1989c, Radziszowski and Kreher 1988
3	11	[46, 51]	Radziszowski and Kreher 1988
3	12	[52, 59]	Exoo 1993, Radziszowski and Kreher 1988, Exoo 1998, Lesser 2001
3	13	[59, 69]	Piwakowski 1996, Radziszowski and Kreher 1988

5	5	[43, 49]	Exoo 1989b, McKay and Radziszowski 1995
6	6	[102, 165]	Kalbfleisch 1965, Mackey 1994
7	7	[205, 540]	Hill and Irving 1982, Giraud 1973
```

Guess: for any ineteger n>=1, RamseyNumber(n+1,n+1)-1 = S(n,n) contains only the factors of Fermat Numbers ` F[m]=2^2^m+1 `, {1,2,3,5,17,257,641,65537,...}
现在地球居民都知道 S(2,2)=5, S(3,3)=17, 我猜 S(4,4)=45, S(5,5)=

- try to prove Twin Prime Conjecture
```
    1. Method 1: If a prime gap subsequence repeats twice, then it will occur infinitely times. 
    such as {2}, {4},{2*k},{2,4,2},{6,6}...
    2. Method 2: by using modern database function `groupby` on prime gap sequence, ...  
     Observing prime gap frequency distribution for primes up to some big integer N0 .  
     Peaks occur at multiples of 6. And the ratio of {2}s to {6}s will be great than a const(0.5 ?).
    1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, 4, 6, 2, 10, 2, 6, 6, 4, 6, 6, 2, 10, 2, 4, 2, 12, 12, 4, 2, 4, 6, 2, 10, 6, 6, 6, 2, 6, 4, 2, ... (sequence A001223 in the OEIS).
```

- define the integer sequence `x[n+1]:=x[n]^2+1`, if take x[0]>1, then  x[5] is always composite, never be prime. I guess that x[k] can always be written as another form of two square sum, k>=5.

- try to prove 3n+1 Conjecture: 
```
def f(n):
    while n%2==0 : n/=2
    n=3*n+1
    while n%2==0 : n/=2
    return n

思路: for any odd integer n, before the steps=ceil(log(3,4^n))=ceil(n*log(3,4)) calling f(n), 
it will return a less number m, m<n .  
在大约n*log(3,4)次嵌套调用f(n)之前，总会得到一个比n更小的数m，
从而由归纳法推出Collatz Conjecture 对所有正整数都成立。
```

- 定义:二密分解 `n=q1*q2` , `q1`取小于或等于`√n`的最大因数, `q2`取大于或等于`√n`的最小因数。
是否值得尝试，使用二密分解或p-密分解的一些性质证明费马大定理? 抛开Wiles的复杂理论和过程?


#### 赞助支持
<img src="temp/1563593535473.jpg" width="280">
<img src="temp/mm_facetoface_collect_qrcode_1560552098216.png" width="280">

感谢你的赞助和支持，希望你我每天都能做得更好！！！