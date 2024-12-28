const Comment1 = () =>{
    fetch('https://jsonplaceholder.typicode.com/comments')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.error('error happen',error))             /// catch error if any happens
}






// by using async() function                same work 




/* const  Comment2 =   async()   =>{
    const res = await fetch('https://jsonplaceholder.typicode.com/comments');
    const data = await res.json();
    console.log(data)
} */


const  Comment2 =   async()   =>{
    try{
        const res = await fetch('https://jsonplaceholder.typicode.com/comments');
        const data = await res.json();
        console.log(data)
    }
    catch(error){
        console.error('data load error!!!')
    }
} 