import re
from typing import List, Optional
from back.ast.nodes import Node, Const, Var, Add, Mul, Pow

# Token con tipo y valor
class Token:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type!r}, {self.value!r})"

_TOKEN_REGEX = re.compile(r"\s*(?:(\d+)|([A-Za-z]+)|(\^|\*|\+|\-|\(|\)))")

class Parser:
    def __init__(self, text: str):
        self.tokens = self._tokenize(text)
        self.pos = 0

    def _tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []
        for num, var, op in _TOKEN_REGEX.findall(text):
            if num:
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
