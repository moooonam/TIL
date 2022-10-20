 // 3-1
 const defaultColors = ['red', 'green', 'blue'];
 const favoriteColors = ['navy', 'black', 'gold', 'white']
 const palette = [...defaultColors, ...favoriteColors]
 console.log(palette)
 
 // 3-2
 const info1 = { name: 'Tom', age: 30 }
 const info2 = { isMarried: true, balance: 3000 }
 const fullInfo = {...info1, ...info2}
 console.log(fullInfo)