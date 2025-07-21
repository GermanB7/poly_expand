from back.algebra.polynomial import Polynomial
from back.algebra.term import Term

def term_to_str(term: Term) -> str:
    parts = []
    coeff = term.coeff

    # Si el coeficiente es ±1 y hay variables, lo omitimos o solo ponemos '-'
    if term.exponents:
        if coeff == -1:
            coeff_str = "-"
        elif coeff == 1:
            coeff_str = ""
        else:
            coeff_str = str(coeff)
    else:
        coeff_str = str(coeff)

    parts.append(coeff_str)

    for var, exp in sorted(term.exponents.items()):
        if exp == 1:
            parts.append(var)
        else:
            parts.append(f"{var}^{exp}")  # sin llaves
    return "".join(parts)



def polynomial_to_latex(poly: Polynomial) -> str:
    if not poly.terms:
        return "0"
    latex_parts = [term_to_str(term) for term in poly.terms]
    return " + ".join(latex_parts).replace("+ -", "- ")
