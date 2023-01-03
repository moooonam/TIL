// function add(num1, num2) {
//     return num1 + num2    
// }

// console.log(add(2, 7))

// const sub = function (num1, num2){
//     return num1 - num2
// }

// console.log(sub(7, 2))

// const greeting = function (name){
//     return `Hi ${name}`
// }

// // 1단계
// const greeting = (name) => {
//     return `Hi ${name}`
// }

// // 2단계
// const greeting = name => {
//     return `Hi ${name}`
// }

// // 3단계
// const greeting = name => `Hi ${name}`



const numbers =[1, 2, 3, 4, 5]
console.log(numbers[0])
console.log(numbers[2])
console.log(numbers.length)

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join('-'))