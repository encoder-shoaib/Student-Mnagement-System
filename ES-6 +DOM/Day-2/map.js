
const number = [1,2,3,4,5,6,7];

function doubles(n){
    return n*2;
}

for (const num of number){
    console.log(doubles(num));
}

console.log("*******************************************");
// by map 😁😁😁😁😁😁😁


// map function take a array or object and read all property then return as a array'😒 

const double = (x) => x*2;

const result = number.map(double)
console.log(result)



console.log("*******************************************");

// 🫡🫡🫡🫡shortcut🫡🫡🫡🫡🫡

const result1 = number.map(n => n*2);
console.log(result1)




// more 😒😒😒😒😒😒😒😒😒😒😒😒😒😒 


const friends = ['shoaib','abir','dipto','ashik','rifat','debu'];

const length = friends.map(friend => friend.length);
console.log(length)                                  //===>>> [ 6, 4, 5, 5, 5, 4 ]


const firstLetter = friends.map(friend => friend[0])
console.log(firstLetter);                           // ====>>>> [ 's', 'a', 'd', 'a', 'r', 'd' ]