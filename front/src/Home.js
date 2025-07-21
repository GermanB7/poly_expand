import "./App.css";
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();
  return (
    <div className="App div-centrada">
      <div className="titulo-container">
        <h1>EXPANSOR DE</h1>
        <h1 className="titulo-secundario">EXPRESIONES-3000</h1>
      </div>

      <div className="descripcion">
        <p>Se reescribirá la expresión escrita</p>
        <p>como producto de factores, a un</p>
        <p>polinomio simplificado</p>
      </div>

      <button className="yellow-button" onClick={() => navigate('/calculadora')}>
        Iniciar
      </button>
    </div>
  );
}