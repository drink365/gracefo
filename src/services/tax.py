
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# 預設台灣遺產稅累進稅率（示意，可於 UI 調整）：
# 0~50,000,000 → 10% ; 50,000,001~100,000,000 → 15% ; 100,000,001+ → 20%
DEFAULT_BRACKETS: List[Tuple[float, float]] = [
    (50_000_000.0, 0.10),
    (100_000_000.0, 0.15),
    (float('inf'), 0.20),
]

@dataclass
class EstateTaxInput:
    net_estate: float                  # 淨遺產（總遺產 - 債務 - 扣除）
    basic_exemption: float = 12_000_000.0
    brackets: List[Tuple[float, float]] = field(default_factory=lambda: DEFAULT_BRACKETS)

def calc_estate_tax_progressive(inp: EstateTaxInput) -> Dict[str, float | list]:
    taxable_base = max(inp.net_estate - inp.basic_exemption, 0.0)
    remain = taxable_base
    last_threshold = 0.0
    total_tax = 0.0
    details = []  # 每級課稅明細

    for threshold, rate in inp.brackets:
        span = min(remain, threshold - last_threshold)
        if span > 0 and remain > 0:
            tax = span * rate
            details.append({
                "區間起": last_threshold,
                "區間迄": threshold,
                "稅率": rate,
                "課稅額": span,
                "稅額": tax,
            })
            total_tax += tax
            remain -= span
        last_threshold = threshold
        if remain <= 0:
            break

    eff_rate = total_tax / inp.net_estate if inp.net_estate > 0 else 0.0
    return {"taxable": taxable_base, "tax": total_tax, "effective_rate": eff_rate, "details": details}
