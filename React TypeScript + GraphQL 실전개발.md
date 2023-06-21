# React TypeScript + GraphQL 실전개발

<hr>

- app.tsx (라우터 쓰는법)
```tsx
import Home from "./routes/Home";
import About from "./routes/About";
import Nav from "./components/Nav";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <>
      <Router>
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />       
          <Route path="/about" element={<About />} />
     
        </Routes>
      </Router>
    </>
  );
}

export default App;
```

- 이런식으로 구성 path에 내가 원하는 경로 넣고 element에 컴포넌트 넣기
- Router v6 부터는 exact 는 더이상 사용하지 않고 여러 라우팅을 매칭하고 싶은 경우 URL 뒤에 * 을 사용합니다.

<hr>

- Link로 프롭 넘기기
```tsx
// RouterProp
import { Link } from "react-router-dom"
const RouterPropTest = () => {
    const menu = {
        name: "간짜장",
        price: "5000원",
    }
    return (
        <div>
            <h1>Router Prop Test</h1>
            <Link to={"/routerproptestresult"} state={menu}>데이터 날리기</Link>
        </div>
    );
};

export default RouterPropTest;

// RouterPropsResult

import { useLocation } from "react-router-dom"

interface propTypes {
        name: string,
        price: string
}
const RouterPropTestResult = () => {
    const location = useLocation()
    const state = location.state as propTypes
    console.log(state)

    return (
        <>
            <h1>Router Prop Test Result</h1>

            {state ? (<div>
                <div>{state.name}</div>
                <div>{state.price}</div>
                    </div>)
                : <div></div>
            }

        </>
    );
};

export default RouterPropTestResult;
```