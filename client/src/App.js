import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Result from "./pages/Result";

function App() {
  return (
    <BrowserRouter>
      <Routes path="/">
        <Route index element={<Home/>}/>
        <Route path="result" element={<Result/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
