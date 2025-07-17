from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from poly_expand.algebra.term import Term

@dataclass
class Polynomial:
    terms: list[Term]

    def __post_init__(self):
        # Normalizar: agrupar términos y eliminar coeficientes cero
        grouped: dict[tuple[tuple[str,int], ...], int] = defaultdict(int)
        for term in self.terms:
            # clave: tupla ordenada de pares (var, exp)
            key = tuple(sorted((v, e) for v, e in term.exponents.items() if e != 0))
            grouped[key] += term.coeff
        # reconstruir lista de Terms
        self.terms = [
            Term(coeff, {v: e for v, e in key})
            for key, coeff in grouped.items() if coeff != 0
        ]
        # orden canónico: por exponente total descendente, luego lex
        self.terms.sort(key=lambda t: (-sum(t.exponents.values()), tuple(sorted(t.exponents.items()))))

    def __add__(self, other: Polynomial) -> Polynomial:
        return Polynomial(self.terms + other.terms)

    def __mul__(self, other: Polynomial) -> Polynomial:
        products: list[Term] = []
        for t1 in self.terms:
            for t2 in other.terms:
                # multiplicar coeficientes
                new_coeff = t1.coeff * t2.coeff
                # sumar exponentes
                exps: dict[str,int] = {}
                for v, e in t1.exponents.items():
                    exps[v] = exps.get(v, 0) + e
                for v, e in t2.exponents.items():
                    exps[v] = exps.get(v, 0) + e
                products.append(Term(new_coeff, exps))
        return Polynomial(products)

    def __repr__(self) -> str:
        if not self.terms:
            return "0"
        return " + ".join(repr(t) for t in self.terms).replace("+ -", "- ")
