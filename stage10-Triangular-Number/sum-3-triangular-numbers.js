//generate table of 3 tris sum below MAX.
//run this code to get a csv file by
//node sum-3-triangular-numbers.js > 3-tris-sum.csv

const MAX=25, MAXS=MAX*(MAX+1)/2;
let T=[],arr=[],sum=0;
//Array(100).fill(0)
for (let i = 0; i <= MAX; i++) {
    let tri=i*(i+1)/2;
    T.push(tri);     
}

for (let i = 0; i <= MAXS; i++) {
    arr.push([i,'','','']);
}

console.log(`n, 'one-tri', 'two-tris', 'three-tris'`);
for (let a = 1; a <= MAX; a++) {
    arr[T[a]][1]=a;
    for(let b = 1,sum=T[a]+T[b]; b <= a && sum<=MAXS; b++,sum=T[a]+T[b]) {     
        arr[sum][2]+=`${a} ${b}|`;
        for(let c = 1,sum=T[a]+T[b]+T[c]; c <= b && sum<=MAXS; c++,sum=T[a]+T[b]+T[c]) {     
            arr[sum][3]+=`${a} ${b} ${c}|`;
           
        }
        
    }

}

//require('util').inspect.defaultOptions.maxArrayLength = MAXS+1;
arr.forEach(element => {
    console.log(`${element[0]}, '${element[1]}', '${element[2]}', '${element[3]}'`) 
});

