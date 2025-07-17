import pytest
from poly_expand.ast.nodes import Const, Add
from poly_expand.ast.visitor import NodeVisitor

class DummyVisitor(NodeVisitor):
    def visit_Const(self, node: Const):
        return node.value * 2

    def visit_Add(self, node: Add):
        return self.visit(node.left) + self.visit(node.right)

def test_dummy_visitor_const():
    v = DummyVisitor()
    assert v.visit(Const(4)) == 8

def test_dummy_visitor_add():
    v = DummyVisitor()
    expr = Add(Const(2), Const(3))  # 2*2 + 3*2 = 4+6 = 10
    assert v.visit(expr) == 10

def test_visitor_missing_method():
    class Incomplete(NodeVisitor):
        pass
    with pytest.raises(NotImplementedError):
        Incomplete().visit(Const(1))
