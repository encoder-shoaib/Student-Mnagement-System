const data = [{id:23 , name: "shaoib" , address: 'kamarali'}]

// console.log(data.id)
console.log(data[0].id,data[0].name,data[0].address)

console.log('********************************')

const product = {
    name: 'laptop',
    brand: [
        { name: 'hp', color: 'black', price: 34234 },
        { name: 'apple', color: 'silver', price: 114234 }
    ]
};

console.log(product.brand[1].name,product.brand[1].price)

console.log('********************************')


const user1 = {
    address : {
        street : {
            frist : "kamarali ",
            second : "kalaroa",
            third: "satkhira",
        }
    }
}
const user2 = {
    address : {   
        frist : "kamarali ",
        second : "kalaroa",
        third: "satkhira",

    }
}


console.log('********************************')

// if i use same line for call 

console.log(user1.address.street.second)
console.log(user2.address.street?.second)   //kalaroa  /* undefined */


