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
    - $와 중괄호 ($ {expression})로 표기하여 표현식 가능(파이썬의 f-string이랑 비슷)
  
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


