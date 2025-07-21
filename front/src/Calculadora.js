import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";
import ImgRespuesta from "./assets/ImgRespuesta.png";

export default function Calculadora() {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState("");
  const [mostrarResultado, setMostrarResultado] = useState(false);
  const [resultado, setResultado] = useState("");
  const [latex, setLatex] = useState("");
  const [error, setError] = useState("");

  const handleCalcular = async () => {
    setMostrarResultado(false);
    setError("");
    setResultado("");
    setLatex("");
    try {
      const res = await fetch("http://localhost:5000/expand", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ expression: inputValue })
      });
      const data = await res.json();
      if (res.ok) {
        setResultado(data.result);
        setLatex(data.latex);
        setMostrarResultado(true);
      } else {
        setError(data.error || "Error desconocido");
      }
    } catch (err) {
      setError("No se pudo conectar con el servidor");
    }
  };

  return (
    <div className="calculadora-contenedor">
      <h1 className="titulo">Escribe la expresión acá</h1>
      <p className="subtitulo">Recuerda que es en formato LaTeX</p>

      <input
        id="exp_producto"
        type="text"
        placeholder="(x - r_1)(x - r_2)..."
        className="input-texto"
        onChange={(e) => setInputValue(e.target.value)}
      />

      <div className="botones">
        <button className="orange-button" onClick={() => navigate("/")}>
          Volver
        </button>
        <button className="yellow-button" onClick={handleCalcular}>
          Calcular
        </button>
      </div>

      {error && (
        <div className="error" style={{ color: 'red', marginTop: '1rem' }}>{error}</div>
      )}
      {mostrarResultado && (
        <div className="resultado">
          <div className="output-texto">Expansión: {resultado}</div>
          <div className="output-latex">LaTeX: <span style={{fontFamily:'monospace'}}>{latex}</span></div>
        </div>
      )}
    </div>
  );
}