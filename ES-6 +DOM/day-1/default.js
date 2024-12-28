function add (num1 ,num2 ){
    const sum = num1 + num2;
    console.log(sum)
}

add(4,6)

// /* add(4) */ NaN

function sum (num1=0 ,num2=0 ){
    const sum = num1 + num2;
    console.log(sum)
}

sum(4,66)
sum(4)
sum()


// for string 

function fullName(firstName , lastName){
    console.log(firstName + ' ' +  lastName)
}

fullName('shaoib','ahammed')

// Default 

function fullNameBYDefault(firstName='' , lastName =''){
    console.log(firstName + ' ' +  lastName)
}

fullNameBYDefault('shaoib','ahammed')
fullNameBYDefault('shoaib')



// for array 

function friends (name = []){

}


// for object 

function person (human={}){
    
}
