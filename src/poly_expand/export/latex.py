from poly_expand.algebra.polynomial import Polynomial
from poly_expand.algebra.term import Term

def term_to_str(term: Term) -> str:
    parts = []
    coeff = term.coeff
    # Coeficiente 1 o -1
    if term.exponents and abs(coeff) == 1:
        coeff_str = "-" if coeff < 0 else ""
    else:
        coeff_str = str(coeff)
    parts.append(coeff_str)
    # Variables ordenadas
    for var, exp in sorted(term.exponents.items()):
        if exp == 0:
            continue
        if exp == 1:
            parts.append(var)
        else:
            parts.append(f"{var}^{{{exp}}}")
    return "".join(parts)

def polynomial_to_latex(poly: Polynomial) -> str:
    if not poly.terms:
        return "0"
    latex_parts = []
    for term in poly.terms:
        latex_parts.append(term_to_str(term))
    expr = " + ".join(latex_parts)
    return expr.replace("+ -", "- ")
