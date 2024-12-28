const glass ={
    name : 'glass',
    color : 'black',
    price : 170,
    isClean : true
}

console.log(glass)


// keys
const key = Object.keys(glass)
console.log(key)                     // [ 'name', 'color', 'price', 'isClean' ]

// values
const value = Object.values(glass)
console.log(value)              //  [ 'glass', 'black', 170, true ]

// entries
const pair = Object.entries(glass)
console.log(pair); 

// Answer = > this is array of array or 2 dymentional array 
/* [
    [ 'name', 'glass' ],
    [ 'color', 'black' ],
    [ 'price', 170 ],
    [ 'isClean', true ]
  ] */


    // delete 
console.log(glass)     //{ name: 'glass', color: 'black', price: 170, isClean: true }
delete glass.isClean;
console.log(glass)  //{ name: 'glass', color: 'black', price: 170 }



// ... 

const {color, ...shortGlass} =glass;
console.log(shortGlass)       //   { name: 'glass', price: 170 }




glass.source = 'Bangladesh';
console.log(glass)    //{ name: 'glass', color: 'black', price: 170, source: 'Bangladesh' }





// seal  use not delete , not add , but u can update 
Object.seal(glass)
glass.model = 'Akiz';
glass.price = 55555;

console.log(glass)

// freeze 
Object.freeze(glass)
glass.model = 'Akiz';
console.log(glass)    //{ name: 'glass', color: 'black', price: 170, source: 'Bangladesh' }  this will not add 

