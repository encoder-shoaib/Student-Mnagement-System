const product = [
    {id: 1 , name: 'lanavo', price : 34324},
    {id: 2 , name: 'hp', price : 74324},
    {id: 1 , name: 'mac', price : 134324},
]

// map 

const names = product.map(product => product.name)
console.log(names)     //[ 'lanavo', 'hp', 'mac' ]

const prices = product.map(p => p.price)
console.log(prices)         //[ 34324, 74324, 134324 ]


// forEach

product.forEach(element => console.log(element.id));         //1  2 1


// Filter

const expensive = product.filter(p => p.price > 100000)
console.log(expensive)        //[ { id: 1, name: 'mac', price: 134324 } ]


console.log('***********************')

// Find

const expensiveProduct = product.find(p => p.price > 10000)
console.log(expensiveProduct)        //{ id: 1, name: 'lanavo', price: 34324 }


// reduce 

const total = product.reduce((p,c)=>p + c.price ,0)
console.log(total)             //   242972