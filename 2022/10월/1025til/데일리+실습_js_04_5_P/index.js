// 코드를 작성해 주세요
function randomNum(min, max){
    var randNum = Math.floor(Math.random()*(max-min+1)) + min;
    return randNum;
}

const scissors = document.querySelector('#scissors-button')
const rock = document.querySelector('#rock-button')
const paper = document.querySelector('#paper-button')
const btns = document.querySelectorAll('button')
const sectionTag = document.querySelector('section')
const modalMsg = document.querySelector('.modal-content')
const imgList = ["./img/scissors.png","./img/rock.png","./img/paper.png"]
const modalTag = document.querySelector('.modal')
const count1 = document.querySelector('.countA')
const count2 = document.querySelector('.countB')

let countA = 0
let countB = 0
let resultmsg =""
let i = 0


scissors.addEventListener('click', function (event) {
    document.getElementById("player1-img").src = "./img/scissors.png"
    btns.forEach(btn => {
        btn.disabled = true
    } )

    const timer = setInterval(function () {
        i = (i + 1) % 3
        document.getElementById("player2-img").src = imgList[i]
    }, 100)

    setTimeout(function () {
        clearInterval(timer)
    }, 3000)

    var a = randomNum(0, 2)
    // console.log(a)
    setTimeout(() => {document.getElementById("player2-img").src  = imgList[a]}, 3001)

    if (a === 0) {
        resultmsg = '무승부'
    } else if (a === 1){
        resultmsg = 'player2 승리'
        countB += 1
    } else {
        resultmsg = 'player1 승리'
        countA += 1
    }
    modalMsg.innerText = resultmsg
    setTimeout(() => {modalTag.setAttribute('style','display: flex')
    count1.innerText = countA,
    count2.innerText = countB},
     3500)
})



rock.addEventListener('click', function (event) {
    document.getElementById("player1-img").src = "./img/rock.png"
    btns.forEach(btn => {
        btn.disabled = true
    } )

    const timer = setInterval(function () {
        i = (i + 1) % 3
        document.getElementById("player2-img").src=imgList[i]
    }, 100)

    setTimeout(function () {
        clearInterval(timer)
    }, 3000)

    var a = randomNum(0, 2)
    // console.log(a)
    setTimeout(() => {document.getElementById("player2-img").src  = imgList[a]}, 3001)

    if (a === 0) {
        resultmsg = 'player1 승리'
        countA += 1
    } else if (a === 1){
        resultmsg = '무승부'
    } else {
        resultmsg = 'player2 승리'
        countB += 1
    }
    modalMsg.innerText = resultmsg
    setTimeout(() => {modalTag.setAttribute('style','display: flex')
    count1.innerText = countA,
    count2.innerText = countB},
     3500)
})



paper.addEventListener('click', function (event) {
    document.getElementById("player1-img").src = "./img/paper.png"
    btns.forEach(btn => {
        btn.disabled = true
    } )

    const timer = setInterval(function () {
        i = (i + 1) % 3
        document.getElementById("player2-img").src=imgList[i]
    }, 100)

    setTimeout(function () {
        clearInterval(timer)
    }, 3000)

    var a = randomNum(0, 2)
    // console.log(a)
    setTimeout(() => {document.getElementById("player2-img").src  = imgList[a]}, 3001)

    if (a === 0) {
        resultmsg = 'player2 승리'
        countB += 1
    } else if (a === 1){
        resultmsg = 'player1 승리'
        countA += 1
    } else {
        resultmsg = '무승부'
    }
    modalMsg.innerText = resultmsg
    setTimeout(() => {modalTag.setAttribute('style','display: flex')
    count1.innerText = countA,
    count2.innerText = countB},
     3500)
    
})


modalTag.addEventListener('click', function (event){
    btns.forEach(btn => {
        btn.disabled = false
    } )
    modalTag.setAttribute('style','display: none')
})