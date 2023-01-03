const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
  const i = p1.length
  let k = 0
  while (k < i) {
    if (p1[k] === p2[k]) {
      console.log(0)
      k += 1
    } else if (p1[k] === 'rock' && p2[k] === 'paper') {
      console.log(2)
      k += 1
    } else if (p2[k] === 'rock' && p1[k] === 'paper') {
      console.log(1)
      k += 1
    } else if (p1[k] === 'rock' && p2[k] === 'scissors') {
      console.log(1)
      k += 1
    } else if (p2[k] === 'rock' && p1[k] === 'scissors') {
      console.log(2)
      k += 1
    } else if (p1[k] === 'scissors' && p2[k] === 'paper') {
      console.log(1)
      k += 1
    } else if (p2[k] === 'scissors' && p1[k] === 'paper') {
      console.log(2)
      k += 1
    }
  }
}
console.log(playGame(p1, p2))


