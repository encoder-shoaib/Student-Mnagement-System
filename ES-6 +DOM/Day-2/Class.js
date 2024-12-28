class teacher {
    constructor(name, subject){
        this.name = name;
        this.subject = subject;
    }
    lecture(){
        console.log('sir is teaching math');
    }
}


const papon = new teacher('Papon sir','OS')
console.log(papon)             //teacher { name: 'Papon sir', subject: 'OS' }
papon.lecture()     //sir is teaching math



const Lamiya = new  teacher('Lamiya mem' , 'OOP!!')
console.log(Lamiya)          ///teacher { name: 'Lamiya mem', subject: 'OOP!!' }