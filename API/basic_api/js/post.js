
console.log('this is connected')
function Face_data(){
    url ='https://jsonplaceholder.typicode.com/posts'
    fetch(url)
    .then(res => res.json())
    .then(data => showPost(data))
    
}
function showPost(posts){
    // console.log(post)
    const postContainer = document.getElementById('post-container')
    for(const post of posts ){

        console.log(post)


        const div = document.createElement('div')
        div.classList.add('post')


        div.innerHTML=`
            <h1>user- :${post.userId}</h1>
            <h2>post title : -${post.title} </h2>
            <p>post description:- ${post.body}</p>
        `
        postContainer.appendChild(div);
    }
}

Face_data()