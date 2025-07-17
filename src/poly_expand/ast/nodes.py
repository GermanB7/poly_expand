from __future__ import annotations
from dataclasses import dataclass

# Base para todos los nodos
class Node:
    pass

@dataclass(frozen=True)
class Const(Node):
    value: int

    def __repr__(self) -> str:
        return f"Const({self.value})"

@dataclass(frozen=True)
class Var(Node):
    name: str

    def __repr__(self) -> str:
        return f"Var({self.name!r})"

@dataclass(frozen=True)
class Add(Node):
    left: Node
    right: Node

    def __repr__(self) -> str:
        return f"Add({self.left!r}, {self.right!r})"

@dataclass(frozen=True)
class Mul(Node):
    left: Node
    right: Node

    def __repr__(self) -> str:
        return f"Mul({self.left!r}, {self.right!r})"

@dataclass(frozen=True)
class Pow(Node):
    base: Node
    exp: int

    def __repr__(self) -> str:
        return f"Pow({self.base!r}, {self.exp})"
