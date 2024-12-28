const max1 = Math.max(3,5,7,4,3,4,34,)
console.log(max1)


const num = [1,2,4,6,3,4,54,3];
const max2 = Math.max(num)
console.log(max2)     // this will show NaN


// for this resone we use spread opareto 

const max3 = Math.max(...num)
console.log(max3);



// ***********************************************************************************

const num1 = [1,2,3,4,5,6,7,5]
const num2 = num1;
num2[0]= 7;
console.log(num1)      /*  this will show [    7, 2, 3, 4,    5, 6, 7, 5  ] */
console.log(num2)      /*  this will show [    7, 2, 3, 4,    5, 6, 7, 5  ] */


// for this reson we use 

const cost1 = [1,2,3,4,5,6,7,5]
const cost2 =[...cost1]
cost2[1] = 444;
console.log(cost1)     //[    1, 2, 3, 4,    5, 6, 7, 5  ]
console.log(cost2)      //[   1, 444, 3, 4,   5,   6, 7, 5 ]
