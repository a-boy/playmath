/*!
 * solve_3n+1_probelm.js v1.0.0
 * (c) 2019 Cody Luo (github.com/a-boy)
 * 
 */
var collatz_problem = {
	f: (n) => n % 2 == 1 ? 3 * n + 1 : n / 2,

	//Syracuse function
	g: (n) => {
		while (n % 2 == 0) n /= 2;
		n = 3 * n + 1;
		while (n % 2 == 0) n /= 2;
		return n
	},
    //through nest calling g(x),
	//s0: number of min steps for n to reach a less number m<n
	//s1: number of min steps for n to reach 1 
	s: (n) => {
		if (n == 1) return (0, 0);
		let [step, s0, s1] = [1, 1, 1]
		let x = g(n)
		while (x >= n) {
			x = g(x)
			step++
		}
		s0 = step
		while (x > 1) {
			x = g(x)
			step++
		}
		s1 = step;
		return [s0, s1]
	},
	h: (n) => 4 * n + 1,
	v: (n) => n % 3 == 0 ? null : (n % 3 == 1 ? (4 * n - 1) / 3 : (2 * n - 1) / 3)
}

Object.assign(window, collatz_problem);
/* 
//test Collatz_Conjecture
n=1
while (n<2000000){
    sd=s(n)
    result=[n,f(n),g(n),(3*n+1)/2,sd[0],sd[1]]
    if(sd[0]>=31)
        console.log(result);
    n+=2
}
*/
