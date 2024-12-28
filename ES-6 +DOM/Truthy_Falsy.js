/* Falsy Values:🫡🫡🫡🫡🫡🫡🫡


false
0
-0
0n (BigInt zero)
"" (Empty string)
null
undefined
NaN




Truthy Values: 🫡🫡🫡🫡🫡🫡🫡



true
Any non-zero number
Any non-empty string
" "
Objects (including arrays, functions, etc.)
Symbol()
BigInt (except for 0n) */






// Falsy values
console.log(Boolean(false));    // false
console.log(Boolean(0));        // false
console.log(Boolean(-0));       // false
console.log(Boolean(0n));       // false
console.log(Boolean(""));       // false
console.log(Boolean(null));     // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));      // false

// Truthy values
console.log(Boolean(true));     // true
console.log(Boolean(1));        // true
console.log(Boolean("hello"));  // true
console.log(Boolean([]));       // true
console.log(Boolean({}));       // true
console.log(Boolean(function() {})); // true
console.log(Boolean(Symbol())); // true
console.log(Boolean(42n));      // true

console.log("*********************************************************")



// how to check truthy and falsy value 




// falsy 
const  y = null ;

if(!y){
    console.log('the value is falsy');
}





// truthy 
const z = []

if(!!z){
    console.log('the value is truthy')
}