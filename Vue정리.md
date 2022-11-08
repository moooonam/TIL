# Vue
<hr>

<br>

>### Front-end Framework

<br>

- Front-end(FE) 개발이란?
  - 사용자에게 보여주는 화면 만들기
<br>

- Web App(SPA)를 만들 때 사용하는 도구
<br>

  - SPA (Single Page Application)
    - Web App과 함께 자주 등장할 용어 SPA
    - 이전까지는 사용자의 요청에 적절한 페이지 별 template를 반환
    - SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식을 의미
      - 어떻게 한 페이지로 모든 요청에 대응 할 수 있을까?
      - CSR(Client Side Rendering)방식으로 요청을 처리하기 때문에
<br>

  - Web App이란?
    - 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
    - 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
    - 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태
  - CSR(Client Side Rendering) 이란?
    - 최초 한 장의 HTML을 받아오는 것은 동일
      - 단, server로부터 최초로 받아오는 문서는 빈 html문서
      - 각 요청에 대한 응답을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
        1. 새로운 페이지를 서버에 AJAX로 요청
        2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
        3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)
<br>

  - 왜 CSR 방식을 사용하는 걸까?
    1. 모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문
       - 클라이언트 <-> 서버간 통신 즉, 트래픽이 감소
       - 트래픽이 감소한다 => 응답 속도가 빨라진다.
    2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
       - SNS에서 추천을 누를 때 마다 첫 페이지로 돌아간다 => 끔찍한 App!
       - 요청이 자연스럽게 진행이 된다 = UX 향상
    3. BE와 FE의 작업 영역을 명확히 분리 할 수 있음
       - 각자 맡은 역할을 명확히 분리한다 => 협업이 용이해짐

<br>

  - CSR은 만능일까?
    - 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
  	- 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
    	- 서버가 제공하는 것은 텅 빈 HTML
    	- 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
  	- 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움


<br>
<hr>
<br>


> ### MVVM pattern

<br>

- 소프트웨어 아키텍처 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

![mvvm](https://img1.daumcdn.net/thumb/R750x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbdPccM%2FbtrFzTGgR9K%2FPvfEkR1wM64lJyjWKdytiK%2Fimg.png)

- View => 우리 눈에 보이는 부분 = DOM!
- Model => 실제 데이터 = JSON!
- View Model(Vue)
  - View를 위한 Model
  - View와 연결(binding)되어 Action을 주고 받음
  - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

<br>
<hr>
<br>


> ### Vue instance

<br>

- el(element)
  - Vue instanve와 DOM을 mount(연결)하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id 혹은 class와 마운트 가능
  - Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않은
    - Vue 속성 및 메서드 사용 불가
  - 새로운 Vue instance 생성
  - 생성자 함수 첫번째 인자로 Object 작성
  - el 옵션에 #app 작성 = DOM 연결

<br>

- data
  - Vue instance의 데이터 객체 혹은 인스턴스 속성
  - 데이터 객체는 반드시 기본 객체 {}(Object)여야 함
  - 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  - 정의된 속성은 interpolation {{}}을 통해 view에 렌더링 가능함
  ```html
  <div id="app">
    {{ message }}
  </div>

  <!-- Vue CDN-->
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello, Vue!'
      },
    })
  </script>
  ```

<br>

- methods
  - Vue instance의 method들을 정의하는 곳
  - methods 객체 정의
    - 객체 내 print method 정의
  - method를 호출하여 data 변경 가능
    - 객체 내 bye method 정의
```html
<script>

  const app = new Vue({
    el: '#app',
      data: {
        message: 'Hello, Vue!'
      },
      methods: {
        print: function () {
          console.log(this.message)
        },

        bye: function () {
          this.message = 'Bye, Vue!'
        },
      }
  })
</script>
```

- 주의: methods with Arrow Function
  - 메서드를 정의 할 때, Arrow Function을 사용하면 안됨
  - Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴 즉, this가 상위 객체 window를 가리킴
  - 호출은 문제 없이 가능 하나 this로 Vue의 data를 변경하지 못함

<br>
<hr>
<br>


> ### Directives

<br>

- Directives 기본 구성
  - v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
    - 값에는 JS 표현식을 작성 할 수 있음
  - directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
  - 
![direc](https://vuejs.org/assets/directive.69c37117.png)
- `:` 을 통해 전달인자를 받을 수 있음
- `.` 으로 표시되는 특수 접미사 -directive를 특별한 방법으로 바인딩 해야함

<br>

- v-text
  - Template Interpolation과 함께 가장 기본적인 바인딩 방법
  - {{}} 와 동일한 역할 (정확히 동일한 역할인 것은 아님)
  ```html
  
  <div id="app2">
    <p v-text="message"></p>
    <p>{{ message }}</p>
  </div>
  <script>

   const app2 = new Vue({
      el: '#app2',
      data: {
        message: 'Hello!',
      }
    })
  </script>
  ```

<br>

- v-show
  - 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
    - boolean 값이 변경 될 때 마다 반응
  - 대상 element의 display 속성을 기본 속성과 none으로 toggle
  - 요소 자체는 항상 DOM에 렌더링 됨

- v-if
  - v-show와 사용 방법은 동일
  - isActive의 값이 변경 될 때 반응
  - 단, 값이 false인 경우 DOM에서 사라짐
  - v-if v-else-if v-else 형태로 사용

- v-show VS v-if
  - v-show(Expensive initial load, cheap toggle)
    - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if 보다 높을 수 있음
    - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
  - v-if (Cheap initial load, expensive toggle)
    - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show 보다 낮을 수 있음
    - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가 할 수 있음
```html
<div id="app3">
  <p v-show="isActive">보이니? 안보이니?</p>
  <p v-if="isActive">안보이니? 보이니?</p>
</div>
<script>

  const app3 = new Vue({
    el: '#app3',
      data: {
        isActive: true
      }
    })
</script>
```

<br>

- v-for
  - for .. in .. 형식으로 작성
  - 반복한 데이터 타입에 모두 사용 가능
  - index를 함께 출력하고자 한다면 (char, index)형태로 사용 가능
  - 배열 역시 문자열과 동일하게 사용 가능
  - 각 요소가 객체라면 dot notation으로 접근 할 수 있음
  - **v-for 사용 시 반드시 key 속성을 각 요소에 작성**
  - 각 요소가 고유한 값을 가지고 있지 않다면 생략할 수 있음

```html
<body>
  <!-- 3. v-for -->
  <div id="app">
    <h2>String</h2>
    <div v-for="char in myStr">
      {{ char }}
    </div>
    <div v-for="(char, index) in myStr" :key="index">
      <p>{{ index }}번째 문자열 {{ char }}</p>
    </div>

    <h2>Array</h2>
    <div v-for="(item, index) in myArr" :key="index">
      <p>{{ index }}번째 아이템 {{ item }}</p>
    </div>

    <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
      <p>{{ index }}번째 아이템</p>
		  <p>{{ item.name }}</p>
    </div>

    <h2>Object</h2>
    <div v-for="value in myObj">
      <p>{{ value }}</p>
    </div>

    <div v-for="(value, key) in myObj"  :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        // 1. String
        myStr: 'Hello, World!',

        // 2-1. Array
        myArr: ['python', 'django', 'vue.js'],

        // 2-2. Array with Object
        myArr2: [
          { id: 1, name: 'python', completed: true},
          { id: 2, name: 'django', completed: true},
          { id: 3, name: 'vue.js', completed: false},
			  ],
        
        // 3. Object
        myObj: {
          name: 'harry',
          age: 27
        },
      }
    })
  </script>
</body>
```
<br>

- v-on
  - `:`을 통해 전달받은 인자를 확인
  - 값으로 JS표현식 작성
  - addEventListener의 첫 번째 인자와 동일한 값들로 구성
  - 대기하고 있떤 이벤트가 발생하면 할당된 표현식 실행
  - method를 통한 data조작도 가능
  - mothod에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
  - `@` shortcut 제공
```html
<div id="app">
  <button v-on:click="number++">increase Number</button>
  <p>{{ number }}</p>

  <button v-on:click="toggleActive">toggle isActive</button>
  <p>{{ isActive }}</p>

  <button @click="checkActive(isActive)">check isActive</button>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      number: 0,
      isActive: false,
    },
    methods: {
      toggleActive: function () {
        this.isActive = !this.isActive
      },

      checkActive: function (check) {
        console.log(check)
      }
    }
  })
</script>
```

<br>

- v-bind
  - HTML 기본 속성에 Vue data를 연결
  - class의 경우 다양한 형태로 연결 가능
    - 조건부 바인딩
      - {'class Name':'조건 표현식'}
      - 삼항 연산자도 가능
    - 다중 바인딩
      - ['JS표현식', 'JS표현식',...]
  - Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
  - `:` shortcut 제공
```html
<div id="app2">
  <a v-bind:href="url">Go To GOOGLE</a>

  <p v-bind:class="redTextClass">빨간 글씨</p>  
  <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
  <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>

  <p :class="theme">상황에 따른 활성화</p>
  <button @click="darkModeToggle">dark Mode {{ isActive }}</button>
</div>
<script>
const app2 = new Vue({
  el: '#app2',
    data: {
      url: 'https://www.google.com/',
      redTextClass: 'red-text',
      borderBlack: 'border-black',
      isActive: true,
      theme: 'dark-mode'
    },
    methods: {
      darkModeToggle() {
        this.isActive = !this.isActive
        if (this.isActive) {
          this.theme = 'dark-mode'
        } else {
          this.theme = 'white-mode'
        }
      }
    }
  })
</script>

```

<br>

- v-modle
  - Vue instance와 DOM의 양방향 바인딩
  - Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

<br>

- computed
  - Vue instance가 가진 options중 하나
  - computed 객체에 정의한 한수를 페이지가 최초로 렌더링 될 때 호출하여 계산
    - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반황
- mothod VS computed
  - method
    - 호출 될 때마다 함수를 실행
    - 같은 결과여도 매번 새롭게 계산
  - computed
    - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
    - 종속 대상이 변하지 않으면 항상 저장된 값을 반환

<br>

- filters
  - 텍스트 형식화를 적용할 수 있는 필터
  - interpolation 혹은 v-bind를 이용할 때 사용 가능
  - 필터는 자바스크립트 표현식 마지막에 `|`(파이프)와 함께 추가되어야 함
  - 이어서 사용(chaining) 가능
```html

<body>
  <div id="app">
    <p>{{ numbers | getOddNums }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        getOddNums: function (nums) {
          const oddNums = nums.filter((num) => {
            return num % 2
          })
          return oddNums
        },
      }
    })
  </script>
</body>
```

<br>
<hr>
<br>


> ### Vue Style Guide

<br>

- 우선순위
  - A: 필수(Essential)
    - 오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
    1. v-for는 항상 key와 함께 사용하기
       - 내부 컴포넌트의 상태를 일관되게 유지하기 위해 v-for에 항상 key를 사용하기
       - 데이터의 예측 가능한 행동을 유지 시키기(객체 불변성)
    2. v-for를 쓴 엘리먼트에 절대 v-if를 사용하지 말기
<br>

  - B: 적극권장
    - 규칙을 어겨도 코드는 여전히 실행되겠지만, 규칙 위반은 드물어야 함
<br>

  - C: 권장
    - 일관성을 보장하도록 임의의 선택을 할 수 있음
<br>

  - D: 주의필요
   
<br>
<hr>
<br>


> ### Vue life cycle

<br>

1. created : 뷰 인스턴스 초기화 단계
   - 뷰의 컴포넌트에는 접근이 불가능한 단계, 데이터만 초기화를 한다.
   - 실행 순서 : 상위컴포넌트 => 하위컴포넌트

2. mounted: 컴포넌트를 렌더링 하는 단계
   - 컴포넌트에 접근이 가능해진다.
   - 실행 순서: 하위컴포넌트 => 상위컴포넌트

3. updated : 컴포넌트의 속성들에서 변경이 일어났다거나 또는 어떤 이유로 컴포넌트의 재 랜더링이 일어난 경우에 실행 
  
4. destroyed: 뷰 인스턴스가 제거되는 단계


<br>
<hr>
<br>


> ### Vue CLI

<br>

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 tool 제공
- Vue CLI Quick Start
  - 설치
    - $ npm install -g @vue/cli
  - 프로젝트 생성
    - $ vue create vue-cli
  - Vue 버전 선택
  - 프로젝트 실행
    - npm run serve
- Vue CLI 프로젝트 구조
  - node_modules
    - node.js 환경의 여러 의존성 모듈
    - python의 venv와 비슷한 역할을함 => 따라서 .gitignore에 넣어주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨
  - Module
    - 개발하는 어플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
    - 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이(module) 즉 js파일 하나가 하나의 모듈
    - 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
    - Module 의존성 문제
      - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  - Bundler
    - 모듈 의존성 문제를 해결해주는 작업이 Bundling
    - 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
    - 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러개)로 만들어짐
    - Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
    - snowpack, parcel, rollup.js등의 webpack 이외에도 다양한 모듈 번들러 존재
    - Vue CLI는 이러한 Babel,Webpack에 대한 초기 설정이 자동으로 되어 있음
  - package-lock.json
    - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
    - 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
    - 사용 할 패키지의 버전을 고정
    - 개발 과정 간의 의존성 패키지 충돌 방지
    - python의 requirements.txt 역할
  - src/
    - src/assets
      - 정적 파일을 저장하는 디렉토리
    - src/components
      - 하위 컴포넌트들이 위치
    - src/App.vue
      - 최상위 컴포넌트
      - public/index.html과 연결됨

<br>
<hr>
<br>


> ### Component

<br>

- Vue component 구조
  - 템플릿(HTML)
    - HTML의 body 부분
    - 눈으로 보여지는 요소 작성
    - 다른 컴포넌트를 HTML 요소처럼 추가 가능
  - 스크립트(JavaScript)
    - JavaScript 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨
  - 스타일(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당
  - Vue component 구조 정리
    - 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
    - root에 해당하는 최상단의 component가 App.vue
    - 이 App.vue를 index.html과 연결
    - 결국 index.html 파일 하나만을 rendering
      - 이게 바로 SPA

<br>

- Vue component 실습
  1. src/components/ 안에 생성
  2. script에 이름 등록
  3. template에 요소 추가
```html
// MyComponent.vue
<template>
  <div>
    <h1>This is my component</h1>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',

}
</script>

<style>

</style>
```

- component 등록 3단계
  1. 불러오기
    - import {instanve name} from {위치}
    - instance name은 instance 생성 시 작성한 name
    - @는 src의 shorcut => .vue 생략 가능
  2. 등록하기
  3. 보여주기
    - 닫는 태그만 있는 요소처럼 사용
```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기-->
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
//1. 불러오기
// import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent'

export default {
  name: 'App',
  components: {
    HelloWorld,
    //2. 등록하기
    MyComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

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

<br>
<hr>
<br>

>### Lifecycle Hooks 

<br>

- 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
  - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트하는 경우 등
  - 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
  - 이를 Lifecycle Hooks이라고 함

![lifecycle hooks](https://vuejs.org/assets/lifecycle.16e4c08e.png)

- 실습은 <a href="https://github.com/moooonam/TIL/tree/master/11%EC%9B%94/1107til/lifecyclehook"> 1107til</a> 참고