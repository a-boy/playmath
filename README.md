# playmath
a boy's math playground; math experiment

https://github.com/a-boy/playmath  
https://nbviewer.jupyter.org/github/a-boy/playmath/tree/master/

## Records:
- <b style="color:#0F0"> :star: 2019-09-02, I proved Goldbach's Conjecture!</b>
[stage12-Goldbach%20Conjecture/stage12-try%20to%20prove%20Goldbach%20Conjecture.ipynb](https://nbviewer.jupyter.org/github/a-boy/playmath/blob/master/stage12-Goldbach%20Conjecture/stage12-try%20to%20prove%20Goldbach%20Conjecture.ipynb)  
 _Note: in Sagemath env to run the codes_

	**Goldbach Conjecture Inequality 1**: **`gold(n) < prime_pi(n)+sigma(n,0)`**  
	gold(n): the min non-negative integer `g` makes that both `n-g` and `n+g` are primes  
	prime_pi(n): the count of primes in 1..n  
	sigma(n,0): the count of n.divisors()  

	`gold(n) < prime_pi(n), while n>344`

	`gold(n) < prime_pi(n)*4395/3449751 ≈ prime_pi(n)*0.0013, while n>57989356`

	**Goldbach Conjecture Inequality 2**: **`gold(n) < prime_pi(prime_pi(n)+n)`**	

- <b style="color:#0F0"> :star: 2019-10-28, I solved **3n+1 Problem**!</b> 希望能让Thwaites欣赏并在2019奖励我£1000。

```
# Syracuse function g(n)
def g(n):
    while n%2==0 : n/=2
    n=3*n+1
    while n%2==0 : n/=2
    return n
```

 **Collatz-Syracuse Decent Theorem**: For any odd positive integer n=2*k+1, it exists s1,`s1<=g(n)<=(3*n+1)/2` to make `nest(g,s1,n)==1`;  
Except n=27 or 31, it will get a less number m, m<n before `n` times iterately calling g(x). To be brief,  it exists `s0,s0<n` to make `m= nest(g,s0,n)<n` except n=27 or n=31;  
(n,f(n),g(n),(3*n+1)/2,s(n))  
(27, 82, 41, 41, (37, 41))  
(31, 94, 47, 47, (35, 39))  

 **Collatz正奇数回归树生成规则(Collatz-Odd-Tree Generation Rule)**:

1. 每个节点的长子由 `v(x)=(2*x-1)/3 or (4*x-1)/3` 产生
2. 其余每个小兄弟由 `h(x)=4*x+1` 迭代陆续产生
3. x在完全的Collatz-Odd-Tree中是叶节点 iff (x%3==0)

证明3n+1猜想成立也就只需证明Collatz-Odd-Tree中逆向生成了所有的正奇数。
显然，从`x0=1`出发，通过 `h(x)=4*x+1` 和 `v(x)=(2*x-1)/3 or (4*x-1)/3` 反复迭代，会生成所有形如4k+1和4k-1的数，即所有正奇数。Collatz猜想证明完毕□

- <b style="color:#0F0"> :star: 2018-03-06, I proved Twin Primes Conjecture!</b>
 [stage9-Prime gap subsequence if repeats twice then infinitely times.nb](stage9-Prime%20gap%20subsequence%20if%20repeats%20twice%20then%20infinitely%20times.nb)   

 证明孪生质数猜想，并提出更普遍的规律：任意质数阶差子序列如果出现了两遍就会继续出现无数遍，例如`{2},{4},{2*n},{6,6},{2,4,2},......`

- <b style="color:#0F0"> :star: 2010-02-04, I discovered Prime-Gap-Inequality: The i-th prime gap `p[i+1]-p[i]<=i`</b>

- <b style="color:#0F0"> :star: I discovered Bread Curve and Bread Model by chance in 2011: </b>
  
```
def r(theta):= nest(sin,theta,1000)
polar_plot(r(theta),(theta,0,2*PI))

```
<img src="http://a-boy.tk/playmath/stage2-bread%20curve/bread.png">
<img src="http://a-boy.tk/playmath/stage2-bread%20curve/bread-curve-3d.jpg">

- before2011/果中的泪滴.png  
  <img src="http://a-boy.tk/playmath/before2011/果中的泪滴.png">
- ...
  
## idea:(mailto:a_boy@live.com)
- Prime-Gap-Inequality: The i-th prime gap `p[i+1]-p[i]<=i` . In other words, `range(n,n+primepi(n)+1)` contains one or more primes. So, the i-th prime `p[i]<=1+2+...+ i-1 + p[1] = i*(i-1)/2 +2`
- Bread curve
- `range(n^2, n*(n+1))` contains at least one primes. This is because: as to the array `{n*n, n*n+1, n*n+2, ... ,next_prime(n*n)-1 }`, we can dispatch distinct real factors for every item, these real factors are in `{2,3,4,...,n}` , Pigeonhole principle shows `next_prime(n*n)< n*(n+1)` . Samely, `range(n*(n+1), (n+1)*(n+1))` contains at least one prime. so, this is one sentence proof for 
    ```
    "still unsolved Legendre's conjecture asks whether for every n > 1, there is a prime p, such that n^2 < p < (n + 1)^2 "

    https://en.wikipedia.org/wiki/Legendre%27s_conjecture
    ```
In fact,it holds true that

NextPrime-Square-Inequality; `next_prime_delta(n^2) <= 1+euler_phi(n)`

- Try to prove Goldbach's Conjecture
```
    Except n=344,for any integer n>=2, there exists g=gold(n) , 0=<g<=primepi(n)+1, satisfies that both n-g and n+g are primes. 
    
    ?? because we can dispatch distinct prime factors for {n+1, n+2, ... n+g}.replace( isprime(n+x) => n-x) ?? why n=344 is an exception?
```

- n>=3, let `p=nextprime(n!)-n!` , then p is always prime or 1, because p is less than ` nextprime(n)^2` , very often ` p<n^2 ` .
Conjecture: for any n>=3, ` n! - prevprime(...(prevprime(n!))) ` is always prime or 1, the count of nest `prevprime` can be from 1 to floor(sqrt(n)) times.

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
    1. Method 2: by using modern database function `groupby` on prime gap sequence, ...  
     Observing prime gap frequency distribution for primes up to some big integer N0 .  
     Peaks occur at multiples of 6. And the ratio of {2}s to {6}s will be great than a const(0.5 ?).
    1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, 4, 6, 2, 10, 2, 6, 6, 4, 6, 6, 2, 10, 2, 4, 2, 12, 12, 4, 2, 4, 6, 2, 10, 6, 6, 6, 2, 6, 4, 2, ... (sequence A001223 in the OEIS).
```

- define the integer sequence `x[n+1]:=x[n]^2+1`, if take x[0]>1, then  x[5] is always composite, never be prime. I guess that x[k] can always be written as another form of two square sum, k>=5in.


- 定义:二密分解 `n=q1*q2` , `q1`取小于或等于`√n`的最大因数, `q2`取大于或等于`√n`的最小因数。
是否值得尝试，使用二密分解或p-密分解的一些性质证明费马大定理? 抛开Wiles的复杂理论和过程?

- OPPC(Odd Primes Position Constant) 奇质位常数，`2*k-1`如果是质数则二进制小数点后第k位为1，否则为0

```
const OPPC = 0.0111 0110 1101 0011
               1357 9
```
## Question
- 1/(2*3)+1/(5*7)+1/(11*13)+1/(17*19)+1/(23*29)+... == sum(1/(p[2k-1]*p[2k]), k, 1, oo)==16/75 ? 
 sum(1/k^2, k, 1, oo)==1/6*pi^2 Basel problem solved by Euler
https://math.stackexchange.com/questions/3503866


#### math tools
- Mathematica : .nb is Mathematica notebook
- Sagemath : .ipynb is Jupyter notebook, most of *.ipynb files in a-boy/playmath are used Sagemath, to view by Jupyter nbviewer, but to run codes only in Sagemath env; .sagews is Sagemath worksheet
- Maple
- GeoGebra
- Octave
- MathType
- SketchUp

#### 赞助支持
<img src="temp/1563593535473.jpg" width="280">
<img src="temp/mm_facetoface_collect_qrcode_1560552098216.png" width="280">

感谢你的赞助和支持，希望你我每天都能做得更好！！！
