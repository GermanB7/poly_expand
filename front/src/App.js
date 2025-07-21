import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Calculadora from "./Calculadora";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/calculadora" element={<Calculadora />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;