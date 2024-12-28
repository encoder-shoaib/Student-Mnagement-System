class Vehicle{
    constructor(name,price){
        this.name = name;
        this.price = price;
    }

    move(){
        console.log('gari cole na cole na re !!!')
    }
}


class Bul extends Vehicle{
    constructor(name , price ,seat , ticketPrice){
        super(name,price)
        this.seat = seat;
        this.ticketPrice = ticketPrice;
    }
}

class Track extends Vehicle{
    constructor(name ,price , lode){
        super(name , price)
        this.lode= lode;
    }
}


let car = new Vehicle('car',333333)
console.log(car)     //Vehicle { name: 'car', price: 333333 }