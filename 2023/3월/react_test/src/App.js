import { BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom'
import SimpleBottomNavigation from './pages/Movies';
import Count from './pages/Count';
function App() {
  return (
    <Router>
      <div>
      <Routes>
        <Route path="/movie" element={<SimpleBottomNavigation/>}></Route>
      </Routes>
      <Count></Count>
      </div>
    </Router>
  );
}

export default App;
