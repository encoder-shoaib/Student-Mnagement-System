function greeting(oneMoreFunction , name){
    oneMoreFunction(name);
}




function oneMoreFunction(name){
    console.log('good morning ', name);
}



greeting(oneMoreFunction,'shoaib')