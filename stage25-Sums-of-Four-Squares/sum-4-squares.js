//generate table of 4 squares sum below MAX.
//run this code to get a near csv file.
//node .\sum-4-squares.js >table-4-squares-sum.txt

const MAX=100, MAXS=MAX*MAX;
let s=[],t=[],sum=0;
//Array(100).fill(0)
for (let i = 0; i <= MAX; i++) {
    let square=i*i;
    s.push(square);     
}

for (let i = 0; i <= MAXS; i++) {
    t.push([i,'','','','']);
}

console.log('n, one square, two squares, three squares, four squares')
for (let a = 1; a <= MAX; a++) {
    t[s[a]][1]=a;
    for(let b = 1,sum=s[a]+s[b]; b <= a && sum<=MAXS; b++,sum=s[a]+s[b]) {     
        t[sum][2]+=`${a},${b}|`;
        for(let c = 1,sum=s[a]+s[b]+s[c]; c <= b && sum<=MAXS; c++,sum=s[a]+s[b]+s[c]) {     
            t[sum][3]+=`${a},${b},${c}|`;
            for(let d = 1,sum=s[a]+s[b]+s[c]+s[d]; d <= c && sum<=MAXS; d++,sum=s[a]+s[b]+s[c]+s[d]) {     
                t[sum][4]+=`${a},${b},${c},${d}|`
            }
        }
        
    }

}

require('util').inspect.defaultOptions.maxArrayLength = MAXS+1;

console.log(t)
