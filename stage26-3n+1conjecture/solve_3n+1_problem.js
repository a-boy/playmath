/*!
 * solve_3n+1_probelm.js v1.0.0
 * (c) 2019 Cody Luo (github.com/a-boy)
 * 
 */
 var collatz_problem={
	 f:(n)=> n%2==1? 3*n+1: n/2,
	 
	 //Syracuse function
	 g:(n)=>{ while(n%2==0) n/=2;
		n=3*n+1;
		while(n%2==0) n/=2;
		return n
		},
	//
	 s:0,
	 S:0,
	 h:(n)=> 4*n+1 ,
	 v:(n)=> n%3==0?null:(n%3==1?(4*n-1)/3:(2*n-1)/3)	
 }
 
 Object.assign(window,collatz_problem);

