//var bigInt = require("big-integer");

//Lucas-Lehmer test for primality of 2^p − 1
function is_prime_lucas_lehmer(p){
	let M= 2n**BigInt(p) - 1n
	
	let s = 4n,i=2
	while (i<p)
	{
		s = s*s - 2n
		s%=M
		s2=M-s
		if (s2<s) s=s2;
		i++
		console.log(i)
	}
		
	return s == 0
}

//for(let p of [2,3,5,7,11,13,17,19,23,29,31,37,41])
//	console.log(p,is_prime_lucas_lehmer(p));

let p=82589933
console.log(p,is_prime_lucas_lehmer(p));