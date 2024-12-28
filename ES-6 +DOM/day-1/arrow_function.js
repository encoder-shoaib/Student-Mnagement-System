function add (a , b){
    return a+b;
}

// same as 


const add2 = function(a,b){
    return a + b;
}


// same as 

const add3 = (a,b) => a+b;   // this is arrow function

console.log(add3(4,6))

// more 


const add4 = (a,b,c,d,e) => a+b+c+d+e;

console.log(add4(2,3,4,5,6,))



// same as 

const multiply = (a,b) => a*b;   // this is arrow function

console.log(multiply(4,6))




/* advance  */

// single pramiter
const getAge = (person) => person.name;
const student = {name: 'shoaib',
    id : '234987'
}
console.log(getAge(student))   // shoaib


// single pramiter
const getThirdNumber = number => number[3];
console.log(getThirdNumber([1,2,3,4,5,6,7,]))  //  4



// no pramiter
const getPi = () => Math.PI;
console.log(getPi())          //3.141592653589793


// large Arrow function 

const math =(x,y,z) => {
    const sum = x+y+z;
    const multiply = x*y*z;
    const result = sum + multiply ;
    return result
}

console.log(math(2,3,4,))