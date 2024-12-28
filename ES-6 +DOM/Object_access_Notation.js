const person = {
    name: 'shoaib',
    job : 'WEB DEV',
    skill : {
        1: 'py',
        2: 'js',
        3: 'c'
    },

    'add-ress' : 'kochu khet',
    'home address' : 1270,          

}

console.log(person.name)
console.log(person.job)
console.log(person.skill)

// or ?
console.log(person['job'])           //WEB DEV

console.log(person["add-ress"])          //kochu khet

console.log(person["home address"])      ///1270

/* console.log(person.skill.1) */         /// error because number cant show like this 

console.log(person.skill[1])      // =>py
console.log(person.skill[2])      // =>js
console.log(person.skill[3])      // =>c