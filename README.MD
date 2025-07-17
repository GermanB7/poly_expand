# poly\_expand

Expansión de productos de polinomios a polinomios en Python.

## Descripción

`poly_expand` es un paquete en Python que permite:

1. **Parsear** expresiones de polinomios escritos en sintaxis matemática simple (con enteros, variables, operadores `+`, `-`, `*`, `^` y paréntesis).
2. **Convertir** el árbol de sintaxis (AST) obtenido en un objeto `Polynomial` que representa de forma estructurada la suma de términos.
3. **Expandir** productos de sumas y potencias de polinomios, realizando distribución y agrupación de términos.
4. **Exportar** el resultado final a formato LaTeX para presentación visual.

Este README explica cómo iniciar y comprender cada parte del proyecto.

---

## Requisitos

* Python 3.11 o superior instalado.
* Git (para control de versiones).
* Opcional: GitHub account para repositorio remoto.

---

## Configuración inicial

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/TU_USUARIO/poly_expand.git
   cd poly_expand
   ```

2. **Crear y activar un entorno virtual**

   * Linux/macOS:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   * Windows (PowerShell):

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements-dev.txt
   ```

---

## Estructura del proyecto

```text
poly_expand/
├── .gitignore             # Archivos/dirs ignorados por Git
├── requirements.txt       # Dependencias de runtime (vacío por defecto)
├── requirements-dev.txt   # Dependencias de desarrollo: linters, pytest, mypy...
├── setup.py               # Configuración de empaquetado con setuptools
├── .flake8                # Configuración de Flake8
├── mypy.ini               # Configuración de Mypy
├── pytest.ini             # Configuración de pytest
├── src/                   # Código fuente del paquete
│   └── poly_expand/
│       ├── __init__.py    # Inicializa el paquete
│       ├── ast/           # Definición del AST
│       │   ├── nodes.py       # Clases de nodos: Const, Var, Add, Mul, Pow
│       │   └── visitor.py     # Patrón Visitor base para recorrer nodos
│       ├── algebra/       # Modelo algebraico
│       │   ├── term.py         # Dataclass Term (coeficiente + exponente)
│       │   └── polynomial.py   # Dataclass Polynomial (suma, producto)
│       ├── core/          # Funcionalidad central
│       │   ├── parser.py       # Tokenizador + Parser recursivo
│       │   └── transformer.py  # Convierte AST → Polynomial y expande
│       └── export/        # Exportadores de formato
│           └── latex.py       # Convierte Polynomial → cadena LaTeX
└── tests/                # Pruebas unitarias
    ├── ast/             # Tests para AST
    ├── algebra/         # Tests para Term y Polynomial
    ├── core/            # Tests para parser y transformer
    └── export/          # Tests para exportador LaTeX
```

Cada módulo está diseñado con alta cohesión y bajo acoplamiento:

* **AST (`ast/`)**: Representación intermedia de la expresión.
* **Algebra (`algebra/`)**: Lógica matemática para términos y polinomios.
* **Core (`core/`)**: Orquesta el flujo de parseo y transformación.
* **Export (`export/`)**: Presentación del resultado en LaTeX.

---

## Uso básico

```python
from poly_expand.core.parser import parse
from poly_expand.core.transformer import to_polynomial
from poly_expand.export.latex import polynomial_to_latex

# 1. Parseo
expr_ast = parse("(x+1)*(x-1)")
# 2. Transformación y expansión
poly = to_polynomial(expr_ast)
# 3. Exportar a LaTeX
en_latex = polynomial_to_latex(poly)
print(en_latex)  # Salida: x^2 - 1
```