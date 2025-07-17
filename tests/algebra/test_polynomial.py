import pytest
from poly_expand.algebra.term import Term
from poly_expand.algebra.polynomial import Polynomial

def test_addition_combines_like_terms():
    p1 = Polynomial([Term(1, {'x':1}), Term(2, {'x':1})])
    assert repr(p1) == "3*x"

def test_multiplication_basic():
    p1 = Polynomial([Term(2, {'x':1})])
    p2 = Polynomial([Term(3, {'x':1})])
    assert repr(p1 * p2) == "6*x^2"

def test_zero_polynomial():
    p = Polynomial([Term(1, {}), Term(-1, {})])
    assert repr(p) == "0"

def test_multivariable_and_ordering():
    p = Polynomial([Term(1, {'y':1}), Term(1, {'x':1})])
    # orden: mayor exponente total primero (ambos 1), luego lex: x antes de y
    assert repr(p) == "1*x + 1*y"
