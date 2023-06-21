import Home from "./routes/Home";
import About from "./routes/About";
import Nav from "./components/Nav";
import StudentsList from "./routes/StudentsList";
import StudentDetail from './routes/StudentDetail';

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import RouterPropTest from "./routes/RouterPropTest";
import RouterPropTestResult from './routes/RouterPropTestResult';
function App() {
  return (
    <>
      <Router>
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/routerproptest" element={<RouterPropTest />} />
          <Route path="/routerproptestresult" element={<RouterPropTestResult />} />
          <Route path="/about" element={<About />} />
          <Route path="/studentslist" element={<StudentsList />} />
          <Route path="/studentslist/:id" element={<StudentDetail />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
