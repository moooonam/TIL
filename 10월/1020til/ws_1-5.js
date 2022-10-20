const participantNums = [
  [1, 3, 2, 2, 1],
  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
  [9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35],
];
// console.log(participantNums.length)
for (const i of participantNums) {
  for (const j of i) {
    let count = 0;
    for (const k of i) {
      if (j === k) {
        count += 1;
      }
    }
    if (count == 1) {
      console.log(j);
    }
  }
}

// 3
// 100
// 62
