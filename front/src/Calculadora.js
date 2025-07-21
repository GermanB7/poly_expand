import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";
import ImgRespuesta from "./assets/ImgRespuesta.png";

export default function Calculadora() {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState("");
  const [mostrarResultado, setMostrarResultado] = useState(false);

  const handleCalcular = () => {
    setMostrarResultado(true);
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

       {mostrarResultado && (
        <div className="resultado">
          <div className="output-texto">{inputValue}</div>
          <img
            src={ImgRespuesta}
            alt="Resultado"
            className="imagen-respuesta-cuadro"
          />
        </div>
      )}
    </div>
  );
}