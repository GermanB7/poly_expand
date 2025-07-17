import pytest
from poly_expand.algebra.term import Term
from poly_expand.algebra.polynomial import Polynomial
from poly_expand.export.latex import term_to_str, polynomial_to_latex

def test_term_to_str_basic():
    t = Term(3, {'x':2, 'y':1})
    assert term_to_str(t) == "3x^2y"

def test_term_to_str_unit_coeff():
    t1 = Term(1, {'x':1})
    t2 = Term(-1, {'y':2})
    assert term_to_str(t1) == "x"
    assert term_to_str(t2) == "-y^2"

def test_polynomial_to_latex():
    p = Polynomial([Term(1, {'x':2}), Term(-1, {})])
    assert polynomial_to_latex(p) == "x^2 - 1"

def test_zero_polynomial_latex():
    p = Polynomial([])
    assert polynomial_to_latex(p) == "0"
