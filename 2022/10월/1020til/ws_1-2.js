function palindrome(str) {
  let i = 0
  let j = str.length - 1  //
  while (i <= j) {
    if (str[i] === str[j]){
        // console.log(str[i])
        // console.log(str[j])
        i += 1
        j -= 1
        continue
    } else{
        return false
    }
  }
  if (i >= j) {
    return true
  }
  }
  
  // 출력
  console.log(palindrome('level'))
  console.log(palindrome('hi'))