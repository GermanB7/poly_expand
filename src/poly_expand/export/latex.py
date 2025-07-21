from poly_expand.algebra.polynomial import Polynomial
from poly_expand.algebra.term import Term

def term_to_str(term: Term) -> str:
    from fractions import Fraction
    parts = []
    coeff = term.coeff

    # Mostrar coeficiente como fracción si es decimal
    if isinstance(coeff, float) and not coeff.is_integer():
        frac = Fraction(coeff).limit_denominator(100)
        if frac.numerator == 1 and frac.denominator == 1:
            coeff_str = "1"
        elif frac.numerator == -1 and frac.denominator == 1:
            coeff_str = "-1"
        else:
            coeff_str = f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
    else:
        if coeff == -1 and term.exponents:
            coeff_str = "-"
        elif coeff == 1 and term.exponents:
            coeff_str = ""
        else:
            coeff_str = str(int(coeff)) if isinstance(coeff, float) else str(coeff)

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
