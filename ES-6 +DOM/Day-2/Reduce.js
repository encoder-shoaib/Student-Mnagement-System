const num = [2,4,5,67,5,4,34,3,4,56,4]
const total = num.reduce((previous , current) => previous + current ,0)

console.log(total)      //    ans =====> 188

/* 
previous = previous sum 
current = next number  */