const actor = {
    name : 'shaoib',
    age : 23,
    phone : '01718828688'
}

// destructuring 
// this will help us to re use the code 

const {name} = actor;
console.log(name)

const {name:person , phone} = actor;
console.log(person , phone)



// for array 

const number = [45,56];
const [first , SecondNd] = number;
console.log(first)

// other way 

const [x,y]= [34,3655];
console.log(x,y)



// for function

function doubleTime (a,b){
    return[a*2  , b*2];
}

const [prothom ,diteo] = doubleTime(3,4)
console.log(prothom,diteo);