const numbers = [ 2,4,5,5,3,223,43,63]

const selected = numbers.filter( n => n < 33)
console.log(selected)                //=>>>> [ 2, 4, 5, 5, 3 ] 👏👏👏 take number of input and return an array





const players = [ 2,4,5,5,3,223,43,63,345,6575]

const selecteds = players.filter( n => n > 33)
console.log(selecteds)             //====>>>> [ 223, 43, 63, 345, 6575 ]



// more 😒😒😒😒


const friends = ['shoaib','abir','dipto','ashik','rifat','debu'];

const realFriend = friends.filter( friend => friend.length > 5)
console.log(realFriend)                 // ==>>>> [ 'shoaib' ]

