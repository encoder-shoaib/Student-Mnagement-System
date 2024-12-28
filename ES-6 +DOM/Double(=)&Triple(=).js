
// this is call type coercion 
// so we always use ===

const first = 0
const second = false 

if(first==second){                                  // must use ===
    console.log("the value are same!")
}
else{
    console.log("the value are not equal!")
}



/* when 

first     second    result 

1          true      same
0         false      same

"2"          2        same



            also for ===

{}            {}          Not same 

{x:5}         {x:5}       Not same

[]               []        Not same

 */

// so we use ===