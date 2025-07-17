import pytest
from poly_expand.core.parser import parse
from poly_expand.ast.nodes import Const, Var, Add, Mul, Pow

def test_parse_const():
    assert repr(parse("123")) == "Const(123)"

def test_parse_var():
    assert repr(parse("x")) == "Var('x')"

def test_parse_add():
    assert repr(parse("x+1")) == "Add(Var('x'), Const(1))"

def test_parse_subtraction():
    expr = parse("x-1")
    assert repr(expr) == "Add(Var('x'), Mul(Const(-1), Const(1)))"

def test_parse_mul():
    assert repr(parse("x*1")) == "Mul(Var('x'), Const(1))"

def test_parse_pow():
    assert repr(parse("x^2")) == "Pow(Var('x'), 2)"

def test_precedence_mul_over_add():
    # x+1*2 → Add(Var('x'), Mul(Const(1), Const(2)))
    assert repr(parse("x+1*2")) == "Add(Var('x'), Mul(Const(1), Const(2)))"

def test_parentheses():
    # (x+1)*2 → Mul(Add(Var('x'), Const(1)), Const(2))
    assert repr(parse("(x+1)*2")) == "Mul(Add(Var('x'), Const(1)), Const(2))"

def test_unexpected_character():
    with pytest.raises(SyntaxError):
        parse("x$1")
