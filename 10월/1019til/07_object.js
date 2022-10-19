const myInfo ={
    name: 'jack',
    phoneNumber: '123123',
    'samsung product' : {
        buds: 'Buds pro',
        galaxy: 'S99', 
    },
}
console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].galaxy)


const obj ={
    greeting() {
        console.log('hi!')
    }
}
obj.greeting()







// json 변환

const jsonData ={
    coffee: 'Americano',
    iceCream: 'Mint Choco',
}
// Object -> json
const objToJson = JSON.stringify(jsonData)

console.log(objToJson) //{"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof objToJson) //string

// json -> Object
const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj) //{ coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof jsonToObj) //object

console.log(jsonToObj.coffee) // Americano