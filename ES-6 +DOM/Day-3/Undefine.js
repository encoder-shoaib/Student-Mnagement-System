// 8 Common Ways to Get 'undefined' in JavaScript

// 1. Uninitialized Variable
// A variable that has been declared but not assigned a value will have the value 'undefined'.
let x;
console.log(x); // Output: undefined

// 2. Function with No Return
// A function that doesn't explicitly return a value will return 'undefined' by default.
function test() {}
console.log(test()); // Output: undefined

// 3. Accessing Non-Existent Object Property
// If you try to access a property that doesn't exist on an object, it will return 'undefined'.
const person = { name: "John" };
console.log(person.age); // Output: undefined

// 4. Array Element Out of Bounds
// When you access an index of an array that doesn't exist, it will return 'undefined'.
const arr = [1, 2, 3];
console.log(arr[5]); // Output: undefined

// 5. Function Parameters Not Provided
// If a function is called with fewer arguments than it expects, the missing arguments will be 'undefined'.
function greet(name) {
    console.log(name);
}
greet(); // Output: undefined

// 6. Deleting an Object Property
// Deleting a property from an object will remove it, and if you later try to access the deleted property, it will return 'undefined'.
const person2 = { name: "Alice", age: 30 };
delete person2.age;
console.log(person2.age); // Output: undefined

// 7. Function Arguments Not Passed
// If you call a function with fewer arguments than expected, the unpassed arguments are 'undefined'.
function add(a, b) {
    return a + b;
}
console.log(add(5)); // Output: NaN (because 'b' is undefined)

// 8. Destructuring with Missing Values
// When you destructure an object or array and there are missing properties or elements, the variables are assigned 'undefined'.
const person3 = { name: "Sara" };
const { name, age } = person3; // 'age' is undefined
console.log(age); // Output: undefined
