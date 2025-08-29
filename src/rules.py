# src/rules.py
from typing import Dict

PREFERRED = {
    "governing_law": "Delaware",
    "jurisdiction": "Delaware",
    "max_payment_days": 45,
}

def grade_item(item: Dict) -> str:
    t = item.get("clause_type")
    keys = item.get("key_numbers", {})

    if t == "liability_cap":
        cap = keys.get("cap_multiple_of_fees")
        if cap is None or (cap and cap > 12):
            return "high"

    if t == "payment_terms":
        days = keys.get("payment_days", 0)
        if days > PREFERRED["max_payment_days"]:
            return "medium"

    return "low"
