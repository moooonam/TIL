# JavaScript

<br>
<hr>
<br>

>### 변수와 식별자

<br>

- 식별자 정의와 특징
  - 식별자는 반드시 문자, $, _ 으로 시작
  - 대소문자 구분, 클래스명 외에는 모두 소문자로 시작
  - 카멜 케이스(camelCase, lower-camel-case)
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스(PascalCase, upper-camel-case)
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수에 사용

<br>

- 선언, 할당, 초기화
  - 선언(Declaration)
    - 변수를 생성하는 행위 또는 시점
  - 할당(Assignment)
    - 선언된 변수에 값을 저장하는 행위 또는 시점
  - 초기화(Initialization)
    - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```js
let foo         // 선언
console.log(foo)//undefined

foo = 11        // 할당
console.jog(foo)// 11

let bar = 0     // 선언+할당
console.log(bar)// 0
```

<br>

- 변수 선언 키워드
    1. let
       - 재할당 가능 & 재선언 불가능
       - 블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음
  
    ```js
    // let
    let number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당
    //-------------------------------
    let number = 10 // 1. 선언 및 초기값 할당
    let number = 20 // 2. 재선언 불가능!!
    ```
    
    2. const
        - 재할당 불가능 & 재선언 불가능
        - 선언 시 반드시 초기값을 설정 해야 하며, 이후 값 변경이 불가능
        - let 과 동일하게 블록 스코프를 가짐

    ```js
    // let
    let number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당 불가능!!
    //-------------------------------
    let number = 10 // 1. 선언 및 초기값 할당
    let number = 20 // 2. 재선언 불가능!!
    ```
    3. var
       - 재할당 가능 & 재선언 가능
       - ES6 이전에 변수를 선언할 때 사용되던 키워드
       - *호이스팅*되는 특성으로 인해 예기치 못한 문제 발생 가능
       - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장   

    - 호이스팅(hoisting)
      - 변수를 선언 이전에 참조할 수 있는 현상
      - var 로 선언된 변수는 선언 지전에 참조할 수 있으며 이러한 현상을 호이스팅이라 함
      - 변수 선언 이전의 위치에서 접근시 undefined를 반환
<br>
<hr>
<br>

>### 데이터 타입

<br>

![datatype](https://goodgid.github.io/assets/img/javascript/js_data_types_1.png)

<br>

- Number
  - 정수 또는 실수형 숫자를 표현하는 자료형
  - NaN
    - Not-A-Number(숫자가 아님)를 나타냄
    - Number.isNan()의 경우 주어진 값의 유형이 Number이고 값이 NaN이면 true, 아니면 false를 반환(자바스크립트는 true, false를 파이썬과 다르게 소문자로 준다!!)
- String
  - 문자열을 표현하는 자료형
  - 작음 따옴표 또는 큰 따옴표 모두 가능
  - 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열 붙일 수 있음
  - 줄바꿈 하려면 \n 사용
  - Template Literal을 사용하면 줄바꿈이 되며, 문자열 사이에 변수도 삽입 가능
  - Template literals(템플릿 리터럴)
    - 내장된 표현식을 허용하는 문자열 작성 방식
    - Backtick(``)을 이용
    - `$` 와 중괄호 (`$ {expression}`)로 표기하여 표현식 가능(파이썬의 f-string이랑 비슷)
  
  ```js
  const word =`안녕
  들 하세요`
  console.log(word)

  const age=10
  const message =`홍길동은 ${age}세입니다.`
  console.log(message)
  ```
- Empty Value
  - 갑싱 존재하지 않음을 표현하는 값으로 JavaScript에서는 null 과 undefined가 존재
  - 동일한 역할을 하는 이 두개의 키워드가 존재하는 이유는 단순한 JavaScript의 설계 실수
  - 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장함

- Boolean
  - 참과 거짓을 표현하는 값
  - 조건문 또는 반복문에서 유용하게 사용
    - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 반환됨

<br>
<hr>
<br>

>### 연산자

<br>

- 동등 연산자(==)
  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 비교할 때 *암묵적 타입변환*을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  - <span style="color:red">예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음</span>

<br>

- 일치 연산자(===)
  - 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
  - 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
  - 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

<br>

- 논리 연산자
  - 세 가지 논리 연산자로 구성
    - and 연산은 '&&' 연산자
    - or 연산은 '||' 연산자
    - not 연산은 '!' 연산자

<br>

- 삼항 연산자(Ternary Operator)
  - 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  - 가장 앞의 조건식이 참이면: 앞의 값이 반환되며, 그 반대일 경우 : 뒤의 값이 반환되는 연산자
  - 삼항 연산자의 겨로가 값이기 때문에 변수에 할당 가능
  ```js
  true ? 1 : 2 //1
  false ? 1 : 2 //2

  const result = Math.PI > 4 ? 'Yep' : 'Nope'
  console.log(result) // Nope
  ```

<br>
<hr>
<br>

>### 조건문

<br>

- if statement
  - if,else if, else
  - 조건은 소괄호(condition)안에 작성
  - 실행할 코드는 중괄호{}안에 작선
  - 블록 스코프 생성
  ```js
  const name = 'manager'

  if (name === 'admin'){
    console.log('관리자님 환영합니다.')
  } else if (name == 'manager'){
    console.log('매니저님 환영합니다.')
  } else{
    console.log(`${name}님 환영합니다.`)
  }
  ```
<br>

- switch statement
  - 표현식의 결과값을 이용한 조건문
  - 표현식의 결과값과 case문의 오른쪽 값을 비교
  - break 및 default문은 선택적으로 사용 가능
  - break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
  - 블록 스코프 생성
  ```js
  const name = '홍길동'

  switch(name) {
    case '홍길동' : {
      console.log('관리자님 환영합니다.')
      break
    }
    case 'manager' : {
      console.log('매니저님 환영합니다.')
      break
  }
    default: {
        console.log(`%{name}님 환영합니다.`)
    }
  ```

<br>
<hr>
<br>

>### 반복문

<br>

- while
  ```js
  let i = 0
  
  while (i < 6){
    console.log(i)
    i += 1
  } // 0, 1, 2, 3, 4, 5
  ```

<br>

- for
  ```js
  for ([초기문]; [조건문]; [증감문]) {
    // do something
  }

  for (let i = 0; i < 6; i++){
    console.log(i)
  } //0,1,2,3,4,5
  ```

<br>

- for ... in
  - 객체(object)의 속성을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
  ```js
  const fruits = { a: 'apple', b: 'banana' }
  
  for (const key in fruits){
    console.log(key) // a, b
    console.log(fruits[key]) // apple, banana
  }
  ```
<br>

- for ... of
  - 반복 가능한 객체를 순회할 때 사용
  - 반복 가능한(iterable) 객체의 종류 : Array, Set, String
  ```js
  const numbers = [0, 1, 2, 3]

  for (const number of numbers) {
    console.log(number) // 0, 1, 2, 3
  }
  ```
<br>

- for ... in 과 for ... of 차이
  - for ...in은 속성 이름을 통해 반복
  - for ...of는 속성 값을 통해 반복
  ```js
  const arr = [3, 5, 7]

  for (const i in arr){
    console.log(i) // 0 1 2
  }

   for (const i of arr){
    console.log(i) // 3 5 7
  }
  ```

<br>
<hr>
<br>

>### 함수

<br>

- 함수의 정의
  - 함수 선언식(Function declaration)
    - 일반적인 프로그래밍 언어의 함수 정의 방식
    ```js
    function add(num1, num2) {
      return num1 + num2
    }
    add(2, 7) //9
    ```
  - 함수 표현식(Function expression)
    - 표현식 내에서 함수를 정의하는 방식
    - 함수 표현식은 함수의 이름을 생략함 익명 함수로 정의 가능
    ```js
    const sub = function (num1, num2) {
      return num1 - num2
    }

    sub(7, 2) //5
    ```
    - 표현식에서 함수 이름을 명시하는 것도 가능
    - 다만 이 경우 함수 이름은 호출에 사용 되지 못하고 디버깅 용도로 사용됨
    ```js
    const mySub = function namedSub(num1, num2) {
      return num1 - num2
    }

    mySub(1, 2) //-1
    namedSub(1, 2) // ReferenceError: nameSub is not defined
    ```
  - 기본 인자(Default arguments)
    - 인자 작성 시 '='문자 뒤 기본 인자 선언 가능
    ```js
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }

    greeting() // Hi Anonymous
    ```

<br>

  - 매개변수와 인자의 개수 불일치 허용
    - 매개변수보다 인자의 개수가 많을 경우
    ```js
    const noArgs = function() {
      return 0
    }

    noArgs(1, 2, 3) //0

    const towArgs = function (arg1, arg2){
      return [arg1, arg2]
    }

    towArgs(1, 2, 3) // [1,2]
    ```
    - 매개변수보다 인자의 개수가 적을 경우
    ```js
    const threeArgs = function (arg1, arg2, arg3) {
      return [arg1, arg2, arg3]
    }

    threeArgs()  //[undefined, undefined, undefined]
    threeArgs(1)  //[1, undefined, undefined]
    threeArgs(1, 2)  //[1, 2, undefined]
    ```

<br>

  - Spread syntax(...)
    - "전개 구문"
    - 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음
    1. 배열과의 사용(배열 복사)
    ```js
    let parts = ['shoulders', 'Knees']
    let lyrics = ['head', ...parts, 'and', 'toes']
    // ['head', 'shoulders', 'Knees', 'and', 'toes']
    ```

    2. 함수와의 사용 (Rest parameters)
      - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음
    ```js
    const restOpr = function (arg1, arg2, ...restArgs) {
      return [arg1, arg2, restArgs]
    }

    restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    restArgs(1, 2) // [1, 2, []]
    ```
<br>

  - 선언식과 표현식
    - 선언식 함수와 표현식 함수 타입은 function으로 동일
    - 호이스팅 - 선언식
      - 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생
      - 즉 함수 호출 이후에 선언해도 동작
      ```js
      add(2, 7) //9

      function add (num1, num2) {
        return num1 + num2
      }
      ```
    - 호이스팅 - 표현식
      - 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출시 에러 발생
      - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름
      ```js
      sub(7, 2) //error 어쩌고 저쩌고

      const sub = function (num1, num2) {
        return num1 - num2
      }
      ```
<br>

  - **화살표 함수(Arrow Function)**
    - "함수를 비교적 간결하게 정의할 수 있는 문법"
    - functino 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
      1. function 키워드 생략 가능
      2. 함수의 매개변수가 하나 뿐이라면 매개변수의 '()' 생략가능
      3. 함수의 내용이 한줄이라면 '{}' 와 'return'도 생략 가능
    - 화살표 함수는 항상 익명 함수
    - 화살표 함수 예시
    ```js
    const arrow1 = function (name) {
      return `hello, ${name}`
    }

    // 1. function 키워드 삭제
    const arrow2 = (name) => { return `hello, ${name}` }
    
    // 2. 인자가 1개일 경우에만 () 생략 가능
    const arrow3 = name => { return `hello, ${name}`}

    // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
    const arrow4 = name => `hello, ${name}`

    // 응용
    // 1. 인자가 없다면? () or _로 표시 가능
    let noArge = () => 'No args'
    noArgs = _ => 'No args'

    // 2-1. object를 return 한다면
    let returnObject = () => { return { key: 'value'} }

    // 2-2. return을 적지 않으려면 괄호를 붙여야 함
    returnObject = () => ({key: 'value'})
  
    ```  

<br>
<hr>
<br>

>### 배열(Array)

<br>

- 배열(Array)
  - 키와 속성들을 담고 있는 참조 타입의 객체
  - 순서를 보장하는 특징이 있음
  - 주로 대괄호([])를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
  - 배열의 길이는 array.length 형태로 접근 가능
    - 배열의 마지막 원소는 array.length - 1로 접근
- 배열 메서드 기초
  - array.reverse()
    - 원본 배열 요소들의 순서를 반대로 정렬
  - array.push()
    - 배열의 가장 뒤에 요소 추가
  - array.pop()
    - 배열의 마지막 요소 제거
  - array.includes(value)
    - 배열에 특정 값(value)이 존재하는지 판별 후 true 또는 false 반환
  - array.indexOf(value)
    - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
    - 만약 해당 값이 없을 경우 -1 반환
  - array.join([separator])
    - 배열의 모든 요소를 연결하여 반환
    - separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

<br>

- Array Helper methods
  - 배열을 순회하며 특정 로직을 수행하는 메서드
  - 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
  - callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수
  - forEach
    - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
      - 콜백 함수는 3가지 매개변수로 구성
        1. element: 배열의 요소
        2. index: 배열 요소의 인덱스
        3. array: 배열 자체
      - 반환 값(return) 없음

    ```js
    array.forEach((element, index, array) => {
      // do something
    })
    // 1. 일단 사용해보기
    const colors = ['red', 'blue', 'green']

    printFunc = function (color) {
      console.log(color)
    }
    colors.forEach(printFunc)
    // red
    // blue
    // green

    // 2. 함수 정의를 인자로 넣어보기
    colors.forEach(function (color) {
      console.log(color)
    })

    // 3. 화살표 함수 적용하기
    colors.forEach((color) => {
      return console.log(color)
    })
    
    ```
<br>

  - map
    - 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
    - 기존 배열 전체를 다른 형태로 바꿀 때 유용
      - forEach + return 이라고 생각하기
    ```js
    array.map((element, index, array) => {
      // do something
    })

    // 1. 일단 사용해보기
    const numbers = [1, 2, 3]

    // 함수 정의 (표현식)
    const doubleFunc = function (number) {
      return number * 2
    }

    // 함수를 다른 함수의 인자로 넣기(콜백 함수)
    const doubleNumbers = numbers.map(doubleFunc)
    console.log(doubleNumbers) // [2, 4, 6]

    // 2. 함수 정의를 인자로 넣어보기

    const doubleNumbers = numbers.map(function (number) {
      return number * 2
    }) 
    console.log(doubleNumbers) // [2, 4, 6]

    // 3. 화살표 함수 적용하기

    const doubleNumbers = numbers.map((number) => {
      return number * 2
    })
    console.log(doubleNumbers) // [2, 4, 6]
    ```
<br>

  - filter
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 true인 요소들만 모아서 새로운 배열 반환
    - 기존 배열의 요소들을 필터링할 때 유용
    ```js
    array.filter((element, index, array) => {
      // do something
    })

    const products = [
    { name : 'cucumber', type: 'vagetable' },
    { name : 'banana', type: 'fruit' },
    { name : 'carrot', type: 'vegetable' },
    { name : 'apple', type: 'fruit' },
    ]

    //1.
    const fruitFilter = function (product) {
        return product.type === 'fruit'
    }

    const newArry = products.filter(fruitFilter)

    console.log(newArry)
    // [ { name : 'banana', type: 'fruit' }, { name : 'apple', type: 'fruit' } ]
    //2. 함수 정의를 인자로 넣어보기
    const newArry = products.filter( function (product) {
        return product.type === 'fruit'
    })

    //3. 화살표 함수 적용하기
    const newArry = products.filter((product)=> {
        return product.type === 'fruit'
    })
    ```
<br>

  - reduce
    - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환
    - 즉, 배열을 하나의 값으로 계산하는 동작이 필요한 때 사용(총합, 평균 등)
    - map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
    - reduve 메서드의 주요 매개변수
      - acc
        - 이전 callback 함수의 반환 값이 누적되는 변수
      - initialValue (optional)
        - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
    - reduce의 첫번째 매개변수인 콜백함수의 첫번째 매개변수(acc)는 누적된 값(전 단계 까지의 결과)
    - reduce의 두번째 매개변수인 initialValue 는 누적될 값의 초기값, 지정하지 않을 시 첫번째 요소의 값이 됨
  ```js
  array.reduce((acc, element, index, array) => {
    // do something
  }, initialValue)

  const numbers =[90, 80, 70, 100]

  // 총합

  const sumNum = numbers.reduce(function (result, number) {
      return result + number
  }, 0)

  console.log(sumNum)
  
  ///화살표 함수
  const sumNum = numbers.reduce((result, number) => {
      return result + number
  }, 0)

  //평균
  const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
  ```

<br>

  - find
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 true면, 조건을 만족하는 첫번째 요소를 반환
    - 찾는 값이 배열에 없으면 undefined 반환
  ```js
  array.find((element, index, array)) {
    // do something
  }
  const avengers =[
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32 },
    { name: 'Thor', age: 40 },
  ]

  const avenger = avengers.find((avenger) => {
      return avenger.name ==='Tony Stark'
  })

  console.log(avenger)
  ```
<br>

  - some
    - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 true 반환
    - 모든 요소가 통과하지 못하면 거짓 반환
    - 빈 배열은 항상 false 반환
  ```js
  const arr = [1, 2, 3, 4, 5]

  const result = arr.some((elem) => elem % 2 === 0)

  console.log(result) // true

  ```

<br>

  - every
    - 배열의 모든 요소가 주어진 판별 함수를 통과하면 true 반환
    - 하나의 요소라도 통과하지 못하면 false 반환
    - 빈 배열은 항상 true 반환
  ```js
  const arr = [1, 2, 3, 4, 5]
  const result = arr.every((elem) => elem % 2 === 0)

  console.log(result) // false
  ```

<br>
<hr>
<br>

>### 객체(Object)

<br>

- 개요
  - 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
  - key
    - 문자열 타입만 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
  - value
    - 모든 타입(합수포함)가능
  - 객체 요소 접근
    - 점(.) 또는 대괄호([])로 가능
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
  ```js
  // 객체 예시
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
  
  ```

<br>
<hr>
<br>

>### DOM

<br>

- Browser APIs
  - 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행
  - 종류
    - DOM, Geolocation API, WebGL등

- DOM
  - Document Object Model
  - 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
  - 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
  - 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - DOM은 문서를 논리 트리로 표현
  - DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
  - 웹 페이지는 일종의 문서(document)
  - 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
  - DOM 은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
  - DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음
- DOM에 접근하기
  - DOM을 사용하기 위해 특별히 해야 할 일은 없음
  - 모든 웹 브라우저는 스크립트 언어가 접근할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용함
  - "DOM의 주요객체"들을 활용하여 문서를 조작하거나 특성 요소들을 얻을 수 있음
- DOM의 주요 객체
  - window
  - document
  - navigator, location, history, screen 등
- window object
  - DOM을 표현하는 창
  - 가장 최상위 객체(작성 시 생략 가능)
  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
- document object
  - 브라우저가 불러온 웹 페이지
  - 페이지 컨텐츠의 진입점 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함하고 있음


<br>
<hr>
<br>

>### DOM 조작

<br>

- DOM 조작 순서
  1. 선택(Select)
  2. 조작(Manipulation)
    - 생성, 추가, 삭제 등  

- 선택 관련 메서드
  - document.querySelector(selector)
    - 제공한 선택자와 일치하는 element 한개 선택
    - 제공한 CSS selector를 만족하는 첫번째 element 객체를 반환 (없다면 null 반환)
  - document.querySelectorAll(selector)
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 제공한 CSS selector를 만족하는 NodeList를 반환
    - 참고: NodeList
      - index로만 각 항목에 접근 가능
      - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
      - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

<br>

- 조작 관련 메서드
  - document.createElement(tagName)
    - 작성한 tagName의 HTML 요소를 생성하여 반환
  - Node.innerText
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현
    - 사람이 읽을 수 있는 요소만 남김
    - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  - Node.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 한번에 오직 하나의 Node만 추가할 수 있음
    - 추가된 Node 객체를 반환
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
  - Node.removeChild()
    - DOM에서 자식 Node를 제거
    - 제거된 Node를 반환
  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
  - Element.setAttribute(name, value)
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

- 조작 관련은 <a href="https://github.com/moooonam/TIL/tree/master/10%EC%9B%94/1024til">1024til</a> 참고


<br>
<hr>
<br>

>### Event

<br>

- Event란 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생인데, 우리가 원한다면 그것들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것
  - 예를 들어 사용자가 웹 페이지의 버튼을 클릭한다면 우리는 클릭이라는 사건에 대해 결과를 응답 받기를 원할 수 있음
- 클릭 말고도 웹에서는 각양각색의 Event가 존재
  - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등
- Event object
  - 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  - Event 발생
    - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
    - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
  - DOM 요소는 Event를 받고("수신")
  - 받은 Event를 "처리"할 수 있음
    - Event 처리는 주로 addEventListener()라는 Event 처리기(Event handler)를 다양한 html 요소에 "부착"해서 처리함
- Event handler - addEventListener()
  - "<span style="color:red">대상</span>에 <span style="color:green">특정 Event</span>가 발생하면, <span style="color:blue">할 일</span>을 등록하자"
  - <span style="color:red">EventTarget</span>.addEventListener( <span style="color:green">type</span>, <span style="color:blue">listener</span>)
  - EventTarget.addEventListener(type, listener[, options])
    - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
    - Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상(EventTarget)으로 지정 가능
    - type
      - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
      - 대표 이벤트
        - input, click, submit ....
    - listener
      - 지정된 타입의 Event를 수신할 객체
      - JavaScript function 객체(콜백 함수)여야 함
      - 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음
- 실습은 <a href="https://github.com/moooonam/TIL/tree/master/10%EC%9B%94/1024til">1024til</a> 참고 

<br>

- event.preventDefault()
  - 현재 Event의 기본 동작을 중단
  - HTML 요소의 기본 동작을 작동하지 않게 막음
  - HTML 요소의 기본 동작 예시
    - a 태그: 클릭 시 특정 주소로 이동
    - form 태그: form 데이터 전송

<br>
<hr>
<br>

>### this

<br>

- 어떠한 object를 가리키는 키워드
  - (java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨

<br>

- 전역 문맥에서의 this
  - 브라우저의 전역 객체인 window를 가리킴
    - 전역객체는 모든 객체의 유일한 최상위 객체를 의미
    ```js
    console.log(this) //window
    ```
- 함수 문맥에서의 this
  - 함수의 this 키워드는 다른 언어와 조금 다르게 동작
    - this의 값은 함수를 호출한 방법에 의해 결정됨
  1. 단순호출
    - 전역 객체를 가리킴
    - 전역은 브라우저에서는 window, Node.js는 global을 의미함
  ```js
  const myFunc = function () {
    console.log(this)
  }
  // 브라우저
  myFunc() //window

  // Node.js
  myFunc() // global
  ```
  2. Method(Function in Object, 객체의 메서드로서)
    - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
  ```js
  const myObj = {
    data : 1,
    myFunc() {
        console.log(this)
        console.log(this.data)
    }
  }

  myObj.myFunc() //myObj //1
  ```

<br>
<hr>
<br>

>### 동기와 비동기

<br>

- 동기(Synchronous)
  - 모든 일을 순서대로 하나씩 처리하는 것
  - 순서대로 처리한다 === 이전 작업이 끝나면 다음 작업을 시작한다
  - 우리가 작성했던 Python 코드가 모두 동기식
- 비동기(Asynchronous)
  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
  - 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- 비동기를 사용하는 이유
  - 사용자 경험
    - 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
    - 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
    - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
    - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음

<br>
<hr>
<br>

>### Axios 라이브러리

<br>

- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음
- Axios 사용해보기
  - get,post 등 여러 method 사용가능
  - then을 이용해서 성공하면 수행할 로직을 작성
  - catch를 이용해서 실패하면 수행할 로직을 작성
```js
<script>
  axios.get('요청할 URL')
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백함수)
</script>
```

<br>
<hr>
<br>

>### Callback 과 Promise

<br>

- 비동기 처리의 단점
  - 비동기 처리의 핵심은 Wep API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리한다는 것!
  - 그런데 이는 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음
  - 이와 같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함
  - 어떻게 하냐구? 🤔 => 콜백함수를 사용하자!

<br>

- 콜백함수란?
  - 특별한 함수가 아님! 다른 함수의 인자로 전달되는 함수를 콜백 함수라고 한다.
  - 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
  - 시간이 걸리는 비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용되는 콜백 함수를 비동기 콜백(asynchronous callback)이라 부름
- 콜백 함수를 사용하는 이유
  - 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
  - "요청이 들어오면", "이벤트가 발생하면", "데이터를 받아오면"등의 조건으로 이후 로직을 제어할 수 있음
  - 비동기 처리를 순차적으로 동작할 수 있게 함
  - 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함
- 콜백 지옥(Callback Hell)
  - 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
  - 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용하는데, 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생하게 됨
  - 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 콜백지옥이라 하며, 그때의 코드 작성 형태가 마치 "피라미드와 같다"고 해서 "Pyramid of doom(파멸의 피라미드)"라고도 부름

<br>

- 프로미스(Promise)
  - Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
  - "작업이 끝나면 실행 시켜줄게"라는 약속(promise)
  - 비동기 작업의 완료 또는 실패를 나타내는 객체
  - Promise 기반의 클라이언트가 바로 이전에 사용한 Axios라이브러리!
  - then(callback)
    - 요청한 작업이 성공하면 callback 실행
    - callback은 이전 작업의 성공 결과를 인자로 전달 받음
  - catch(callback)
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달 받음
  - then과 catch 모두 항상 promise 객체를 반환 즉, 계속해서 chaining을 할 수 있음
  - axios로 처리한 비동기 로직이 항상 promise 객체를 반환 그래서 then을 계속 이어 나가면서 작성할 수 있던 것

<br>
<hr>
<br>

>### AJAX

<br>

- AJAX란?
  - 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
  - 이러한 '비동기 통신 웹 개발 기술'을 Asynchronous Javascript And XML(AJAX)라 함
  - AJAX의 특싱
    1. 페이지 새로고침 없이 서버에 요청
    2. 서버로부터 응답(데이터)을 받아 작업을 수행
  - 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

<br>
<hr>
<br>

>### Vuex 

<br>

- State Management
  - 상태(State)란?
    - 현재에 대한 정보(data)
  - 우리는 여러 개의 component를 조합해서 하나의 App을 만들고 있음
  - 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
  - 하지만 결국 이러한 component들이 모여서 하나의 App을 구성할 예정
  - 즉, 여러개의 component가 같은 상태(data)를 유지할 필요가 있음 => 상태관리(State Management) 필요!

- Pass Props & Emit Event
  - 지금까지 우리는 props와 event를 이용해서 상태 관리를 하고 있음
  - 각 컴포넌트는 독립적으로 데이터를 관리
  - 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음
  - 데이터의 흐름을 직관적으로 파악 가능
  - 그러나 component의 중첩이 깊어지면 데이터 전달이 쉽지 않음
  - 공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐

<br>

- Centralized Store
  - 중앙 저장소(store)에 데이터를 모아서 상태 관리
  - 각 component는 중앙 저장소의 데이터를 사용
  - component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
  - 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
  - 규모가 크거나 컴포넌트 중첩이 깊이 프로젝트의 관리가 매우 편리
- Vuex
  - "state management pattern + Library" for vue.js (상태 관리 패턴 + 라이브러리)
  - 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
  - 데이터가 예측 가능한 방식으로만 변경 될 수 있도록하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공
  - Vue의 공식 도구로써 다양한 기능을 제공
  
<br>

- Vuex 시작하기
  - $ vue create vuex-arr => vue 프로젝트 생성
  - $ cd vuex-app => 이동
  - $ vue add vuex => Vue CLI를 통해 vuex plugin 적용

- vuex의 핵심 컨셉 4가지
1. state
  - vue 인스턴스의 data에 해당
  - 중앙에서 관리하는 모든 상태 정보
  - 개별 component는 state에서 데이터를 가져와서 사용
    - 개별 component가 관리하던 data를 중앙 저장소에서 관리하게 됨
  - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
  - **$store.state**로 state 데이터 접근 
2. mutations
  - 실제로 state를 변경하는 유일한 방법
  - vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler)함수는 반드시 동기적이어야 함
    - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
  - 첫 번째 인자로 state를 받으며, component 혹은 Actions에서 commit()메서드로 호출됨 
3. actions
  - mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
  - state를 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경함
  - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음(=== 즉 state를 직접 변경할 수 있지만 하지 않아야 함)
  - component에서 dispatch() 메서드에 의해 호출됨
4. getters
  - vue 인스턴스의 computed에 해당
  - state를 활용하여 계산된 값을 얻고자 할 때 사용
  - state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
  - computed와 마찬가지로 getters의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산됨
  - getters에서 계산된 값은 state에 영향을 미치지 않음
  - 첫번째 인자로 state, 두번째 인자로 getter를 받음


<br>
<hr>
<br>

>### Vuex 실습 

<br>

- 이제부터는 객체 메서드 축약형을 사용할 것!
```js
// before
const obj1 = {
  addValue: function(value){
    return value
  },
}

// after
const obj2 = {
  addValue(value) {
    return value
  },
}
```

- #### state
  - 중앙에서 관리하는 모든 상태 정보
  - $store.state로 접근 가능
  - store의 state에 message 데이터 정의

```js
// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})

```
  - component에서 state 사용

```html
// App.vue

<template>
  <div id="app">
    <h1>{{ $store.state.message }}</h1>
  </div>
</template>

```

- $store.state로 바로 접근하기 보다 computed에 정의 후 접근하는 것을 권장

```html
// App.vue

<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>

export default {
  name: 'App',
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>
```

<br>

- #### actions
  - state를 변경할 수 있는 mutations 호출
  - component에서 dispatch()에 의해 호출됨
  - dispatch(A, B)
    - A:호출하고자 하는 actions 함수
    - B:넘겨주는 데이터(payload) 
  - actions에 정의된 changeMessage 함수에 데이터 전달하기
  - component에서 actions는 dispatch()에 의해 호출됨

```html
<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  },
  data(){
    return {
      inputData: null,
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    },
  },
}
</script>
```
- actions의 첫번째 인자는 context
  - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
  - dispatch()를 사용해 다른 actions도 호출할 수 있음
  - **단, actions에서 state를 직접 조작하는 것은 삼가야 함**
- actions의 두 번째 인자는 payload
  - 넘겨준 데이터를 받아서 사용

```js
// store/index.js

export default new Vuex.Store({
  ...
  actions: {
    changeMessge(context, message) {
      console.log(context)
      console.log(message)
    },
  },
  
})
```
<br>

- #### mutations
  - mutations는 state를 변경하는 유일한 방법
  - component 또는 actions에서 commit()에 의해 호출됨
  - commit(A, B)
    - A: 호출하고자 하는 mutations 함수
    - B: payload
  - mutations 함수의
    - 첫 번째 인자는 state
    - 두 번째 인자는 payload
```js

// stor/index.js
 ...
  mutations: {
    CHANGE_MESSAGE(state, newMessage){
      console.log(state)
      console.log(newMessage)
      state.message = newMessage

    },
  },
  actions: {
    changeMessage(context, newMessage) {
      // console.log(context)
      // console.log(message)
      context.commit('CHANGE_MESSAGE', newMessage)
    },
  },


```

<br>

- #### getters
  - getters는 state를 활용한 새로운 변수
  - getters 함수의
    - 첫 번째 인자는 state
    - 두 번째 인자는 getters

```js
// store/index.js
...
 getters: {
    messageLength(state) {
      return state.message.length
    },
  },
```

  - getters 출력하기
    - getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장
``` html
// App.vue
<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>{{ messageLength }}</h2>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>
<script>
  ...
  computed: {
    message() {
      return this.$store.state.message
    },
    messageLength(){
      return this.$store.getters.messageLength
    }
  },
</script>
``` 