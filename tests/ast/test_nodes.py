import pytest
from poly_expand.ast.nodes import Const, Var, Add, Mul, Pow

def test_const_repr():
    c = Const(5)
    assert repr(c) == "Const(5)"

def test_var_repr():
    v = Var("x")
    assert repr(v) == "Var('x')"

def test_add_repr():
    a = Add(Var("x"), Const(3))
    assert repr(a) == "Add(Var('x'), Const(3))"

def test_mul_and_pow_repr():
    m = Mul(Add(Var("x"), Const(1)), Pow(Var("y"), 2))
    assert repr(m) == "Mul(Add(Var('x'), Const(1)), Pow(Var('y'), 2))"
