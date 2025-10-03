
from dataclasses import dataclass
from typing import Dict

@dataclass
class PolicyPlan:
    annual_premium: float
    pay_years: int
    target_age: int = 90
    projected_cash_value_factor: float = 1.25

def simulate_policy(plan: PolicyPlan) -> Dict[str, float]:
    total_premium = plan.annual_premium * plan.pay_years
    cash_value_90 = total_premium * plan.projected_cash_value_factor
    cp_cash = (cash_value_90 / total_premium * 100) if total_premium > 0 else 0
    return {"total_premium": total_premium, "cash_value_90": cash_value_90, "cp_cash_percent": cp_cash}
