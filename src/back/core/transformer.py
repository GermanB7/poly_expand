
from back.ast.nodes import Node, Const, Var, Add, Mul, Pow
from back.algebra.term import Term
from back.algebra.polynomial import Polynomial


def to_polynomial(node: Node) -> Polynomial:
    """
    Convierte un nodo AST en un objeto Polynomial.
    """
    if isinstance(node, Const):
        # Constante: polinomio de un término constante
        return Polynomial([Term(node.value, {})])
    if isinstance(node, Var):
        # Variable: coef 1, exponente 1 para la variable
        return Polynomial([Term(1, {node.name: 1})])
    if isinstance(node, Add):
        # Suma: polinomio de ambas partes
        left_poly = to_polynomial(node.left)
        right_poly = to_polynomial(node.right)
        return left_poly + right_poly
    if isinstance(node, Mul):
        # Producto: polinomio distribuido
        left_poly = to_polynomial(node.left)
        right_poly = to_polynomial(node.right)
        return left_poly * right_poly
    if isinstance(node, Pow):
        # Potencia: exponenciación binaria simple
        base = to_polynomial(node.base)
        # Empieza con polinomio 1
        result = Polynomial([Term(1, {})])
        for _ in range(node.exp):
            result = result * base
        return result
    raise ValueError(f"Nodo desconocido: {node}")
