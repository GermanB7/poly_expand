from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Term:
    coeff: int
    exponents: dict[str, int]  # p.ej. {'x':2, 'y':1}

    def __repr__(self) -> str:
        # Mostrar para debugging: "3*x^2*y"
        parts = []
        for var, exp in sorted(self.exponents.items()):
            if exp == 0:
                continue
            parts.append(f"{var}^{exp}" if exp != 1 else var)
        vars_part = "*".join(parts)
        if vars_part:
            return f"{self.coeff}*{vars_part}"
        return str(self.coeff)
