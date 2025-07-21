import re
from typing import List, Optional
from poly_expand.ast.nodes import Node, Const, Var, Add, Mul, Pow

# Token con tipo y valor
class Token:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type!r}, {self.value!r})"

_TOKEN_REGEX = re.compile(r"\s*(?:(\d+\.\d+|\d+/\d+|\d+)|([A-Za-z]+)|(\^|\*|\+|\-|\(|\)))")

class Parser:
    def __init__(self, text: str):
        self.tokens = self._tokenize(text)
        self.pos = 0

    def _tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []
        for num, var, op in _TOKEN_REGEX.findall(text):
            if num:
                if '/' in num:
                    tokens.append(Token("FRAC", num))
                elif '.' in num:
                    tokens.append(Token("FLOAT", num))
                else:
                    tokens.append(Token("INT", num))
            elif var:
                tokens.append(Token("VAR", var))
            else:
                tokens.append(Token(op, op))
        return tokens

    def _peek(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _next(self) -> Token:
        tok = self._peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input")
        self.pos += 1
        return tok

    def parse(self) -> Node:
        node = self._parse_expr()
        if self._peek() is not None:
            raise SyntaxError(f"Unexpected token {self._peek()}")
        return node

    def _parse_expr(self) -> Node:
        node = self._parse_term()
        while True:
            tok = self._peek()
            if tok and tok.type == "+":
                self._next()
                right = self._parse_term()
                node = Add(node, right)
            elif tok and tok.type == "-":
                self._next()
                right = self._parse_term()
                # x - y  ≡  x + (-1)*y
                node = Add(node, Mul(Const(-1), right))
            else:
                break
        return node

    def _parse_term(self) -> Node:
        node = self._parse_factor()
        while True:
            tok = self._peek()
            if tok and tok.type == "*":
                self._next()
                right = self._parse_factor()
                node = Mul(node, right)
            else:
                break
        return node

    def _parse_factor(self) -> Node:
        node = self._parse_base()
        tok = self._peek()
        if tok and tok.type == "^":
            self._next()
            exp_tok = self._next()
            if exp_tok.type != "INT":
                raise SyntaxError("Expected integer exponent")
            node = Pow(node, int(exp_tok.value))
        return node

    def _parse_base(self) -> Node:
        tok = self._peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input in base")
        if tok.type == "INT":
            self._next()
            return Const(int(tok.value))
        if tok.type == "FLOAT":
            self._next()
            return Const(float(tok.value))
        if tok.type == "FRAC":
            self._next()
            num, den = tok.value.split('/')
            return Const(float(num) / float(den))
        if tok.type == "VAR":
            self._next()
            return Var(tok.value)
        if tok.type == "(":
            self._next()
            node = self._parse_expr()
            if self._peek() is None or self._peek().type != ")":
                raise SyntaxError("Expected ')'")
            self._next()
            return node
        raise SyntaxError(f"Unexpected token {tok}")

# Función de conveniencia

def parse(text: str) -> Node:
    return Parser(text).parse()

# --- CLI principal ---

def latex_to_algebraic(expr: str) -> str:
    """
    Convierte expresiones simples de LaTeX a notación algebraica.
    Soporta fracciones, paréntesis y potencias.
    Ejemplo: '\left( \frac{1}{2}x + 3 \right)^2' -> '(1/2*x+3)^2'
    """
    import re
    # 1. Fracciones: \frac{a}{b}x -> (a/b)*x
    expr = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}([a-zA-Z])", r"(\1/\2)*\3", expr)
    # 2. Fracciones solas: \frac{a}{b} -> (a/b)
    expr = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"(\1/\2)", expr)
    # 3. Paréntesis LaTeX: \left( ... \right) -> ( ... )
    expr = expr.replace(r"\left(", "(").replace(r"\right)", ")")
    # 4. Eliminar espacios
    expr = expr.replace(" ", "")
    # 5. Potencias: x^{2} -> x^2
    expr = re.sub(r"([a-zA-Z0-9]+)\^\{([0-9]+)\}", r"\1^\2", expr)
    # 6. Multiplicación implícita: entre número/fracción y variable (ej: (1/2)x -> (1/2)*x, 2x -> 2*x)
    expr = re.sub(r"(\([^()]+\)|\d+)([a-zA-Z])", r"\1*\2", expr)
    # 7. Eliminar comandos LaTeX restantes
    expr = re.sub(r"\\[a-zA-Z]+", "", expr)
    # 8. Simplificar paréntesis múltiples: (((a/b)*x)+3)^2 -> ((a/b)*x+3)^2
    expr = re.sub(r"\(\(([^()]+)\)\)", r"(\1)", expr)
    # 9. Balancear paréntesis: si hay desbalance, agregar los que faltan al final
    open_par = expr.count('(')
    close_par = expr.count(')')
    if open_par > close_par:
        expr += ')' * (open_par - close_par)
    elif close_par > open_par:
        expr = '(' * (close_par - open_par) + expr
    return expr

def main():
    import argparse
    from poly_expand.core.transformer import to_polynomial
    from poly_expand.export.latex import polynomial_to_latex
    import sys

    parser = argparse.ArgumentParser(
        description="Expande productos de polinomios y muestra el resultado en texto y LaTeX."
    )
    parser.add_argument(
        "expresion",
        nargs="?",
        help="Expresión polinómica a expandir (ejemplo: (x+1)*(x-1) o LaTeX)"
    )
    parser.add_argument(
        "-l", "--latex", action="store_true", help="Muestra el resultado en formato LaTeX"
    )
    args = parser.parse_args()

    # Leer expresión
    if args.expresion:
        expr = args.expresion
    else:
        print("Introduce la expresión polinómica a expandir:", file=sys.stderr)
        expr = sys.stdin.readline().strip()
        if not expr:
            print("No se recibió ninguna expresión.", file=sys.stderr)
            sys.exit(1)

    # Detectar si es LaTeX y convertir
    expr_proc = expr
    if "\\frac" in expr or "\\left" in expr or "^{" in expr:
        expr_proc = latex_to_algebraic(expr)

    try:
        ast = parse(expr_proc)
        poly = to_polynomial(ast)
    except Exception as e:
        print(f"Error al procesar la expresión: {e}", file=sys.stderr)
        sys.exit(1)

    print("Expansión:")
    print(poly)
    if args.latex:
        print("\nLaTeX:")
        print(polynomial_to_latex(poly))
