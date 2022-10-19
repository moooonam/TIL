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
    