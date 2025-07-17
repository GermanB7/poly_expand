from poly_expand.algebra.term import Term

def test_repr_simple():
    t = Term(3, {'x':2, 'y':1})
    assert repr(t) == "3*x^2*y"

def test_repr_constant():
    t = Term(5, {})
    assert repr(t) == "5"
