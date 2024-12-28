// most of the time we will use const but sum case we use let and we can not use var 
const array = [1,2,3,4,5,6,]
/* array = [1,3,45,55,6,]
console.log(array) */

// but 

array [1] = 5;
array[3] = 9;

console.log(array);


const student = {
    name: 'shoaib',
    id : '33=-224'
}

/* 
student ={name:'abir', id : '4955'
} */

console.log(student)



/* const sum = 0 ;
for (const i =0; i<6; i++){
    sum = sum + i ;
} */

let sum = 0 ;
for (let i = 0; i<6; i++){
    sum = sum + i ;
}

console.log(sum)