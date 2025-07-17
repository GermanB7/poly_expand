from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Term:
    coeff: int
    exponents: dict[str, int]  # p.ej. {'x':2, 'y':1}

    def __repr__(self) -> str:
        if self.coeff == 0:
            return "0"

        parts = []
        for var, exp in sorted(self.exponents.items()):  # orden alfabético
            if exp == 0:
                continue
            parts.append(f"{var}^{exp}" if exp != 1 else var)

        vars_part = "*".join(parts)

        if not vars_part:
            return str(self.coeff)
        elif self.coeff == 1:
            return vars_part
        elif self.coeff == -1:
            return f"-{vars_part}"
        else:
            return f"{self.coeff}*{vars_part}"
