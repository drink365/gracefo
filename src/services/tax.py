
from dataclasses import dataclass
from typing import Dict

@dataclass
class EstateTaxInput:
    net_estate: float
    exemption: float = 12_000_000.0
    rate: float = 0.2

def calc_estate_tax(inp: EstateTaxInput) -> Dict[str, float]:
    taxable = max(inp.net_estate - inp.exemption, 0)
    tax = taxable * inp.rate
    eff_rate = tax / max(inp.net_estate, 1) if inp.net_estate > 0 else 0.0
    return {"taxable": taxable, "tax": tax, "effective_rate": eff_rate}
