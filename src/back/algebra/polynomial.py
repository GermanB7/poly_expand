from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from back.algebra.term import Term

@dataclass
class Polynomial:
    terms: list[Term]

    def __post_init__(self):
        # Normalizar: agrupar términos y eliminar coeficientes cero
        grouped: dict[tuple[tuple[str, int], ...], int] = defaultdict(int)
        for term in self.terms:
            key = tuple(sorted((v, e) for v, e in term.exponents.items() if e != 0))
            grouped[key] += term.coeff
        # reconstruir lista de Terms filtrando coeficientes cero
        self.terms = [
            Term(coeff, {v: e for v, e in key})
            for key, coeff in grouped.items() if coeff != 0
        ]
        # orden canónico: por grado total descendente, luego por exponentes descendentes
        def orden_term(t: Term):
            total_deg = sum(t.exponents.values())
            exp_tuple = tuple(-e for v, e in sorted(t.exponents.items()))
            return (-total_deg, exp_tuple)
        self.terms.sort(key=orden_term)

    def __add__(self, other: Polynomial) -> Polynomial:
        return Polynomial(self.terms + other.terms)

    def __mul__(self, other: Polynomial) -> Polynomial:
        products: list[Term] = []
        for t1 in self.terms:
            for t2 in other.terms:
                new_coeff = t1.coeff * t2.coeff
                exps: dict[str, int] = {}
                for v, e in t1.exponents.items():
                    exps[v] = exps.get(v, 0) + e
                for v, e in t2.exponents.items():
                    exps[v] = exps.get(v, 0) + e
                products.append(Term(new_coeff, exps))
        return Polynomial(products)

    def __repr__(self) -> str:
        if not self.terms:
            return "0"

        def orden(term):
            grado = sum(term.exponents.values())
            nombres_vars = tuple(sorted(term.exponents))
            return (-grado, nombres_vars)

        ordenados = sorted(self.terms, key=orden)

        partes = []
        for term in ordenados:
            coef = term.coeff
            exps = term.exponents

            if not exps:
                partes.append(str(coef))
            else:
                var_part = "*".join(
                    f"{var}^{exp}" if exp != 1 else var
                    for var, exp in sorted(exps.items())
                )
                partes.append(f"{coef}*{var_part}")

        return " + ".join(partes).replace("+ -", "- ")
