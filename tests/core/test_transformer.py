import pytest
from poly_expand.core.parser import parse
from poly_expand.core.transformer import to_polynomial


def test_transform_expand_basic():
    expr = "(x+1)*(x-1)"
    poly = to_polynomial(parse(expr))
    # x^2 - 1
    assert repr(poly) == "1*x^2 - 1"


def test_transform_multivariable():
    expr = "2*x*(x+3*y)"
    poly = to_polynomial(parse(expr))
    # 2*x^2 + 6*x*y
    assert repr(poly) == "2*x^2 + 6*x*y"


def test_transform_power_and_zero():
    expr = "x^3*y^0"
    poly = to_polynomial(parse(expr))
    # y^0 -> constante 1, queda x^3
    assert repr(poly) == "1*x^3"


def test_invalid_node():
    class Dummy(Node):
        pass

    from poly_expand.ast.nodes import Node as AstNode
    # Forcing a wrong type triggers ValueError
    import pytest as _pytest
    with _pytest.raises(ValueError):
        to_polynomial(AstNode())  # Nodo base sin tipo específico
