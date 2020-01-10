function fib(){
	let i=0;
	let [a,b,c]=[0n,1n,1n];
	console.log(a,b,c);
	while (i++<2293)
	{
		a=b+c;b=c+a;c=a+b;
		console.log(a,b,c);
	}
}
fib();