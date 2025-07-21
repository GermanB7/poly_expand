import "./App.css";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import warning from "./assets/warning.png";

export default function Home() {
  const navigate = useNavigate();
  const [errores, setErrores] = useState([{ id: 1 }]);

  const cerrarVentana = (id) => {
    setErrores((prev) => [...prev, { id: prev.length + 1 }]);
    };

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

        {errores.map((e) => (
        <div className="ventana-retro" key={e.id} style={{ top: `${300 + e.id * 20}px`, left: `${200 + e.id * 40}px` }}>
        <div className="ventana-header">
            <span>Windows Installer</span>
            <button onClick={() => cerrarVentana(e.id)}>✕</button>
        </div>
        <div className="ventana-cuerpo">
            <div className="ventana-contenido">
            <img src={warning} alt="Warning" className="icono-warning" />
            <p>
                The Windows Installer Service could not be accessed. <br />
                This can occur if you are running Windows in safe mode, or if the Windows Installer is not correctly installed. <br />
                Contact your support personnel for assistance.
            </p>
            </div>
            <div className="ventana-footer">
            <button onClick={() => cerrarVentana(e.id)}>OK</button>
            </div>
        </div>
        </div>
      ))}
    </div>
  );
}
    