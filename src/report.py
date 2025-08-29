# src/report.py
from typing import List, Dict
from .rules import grade_item

def build_report(items: List[Dict]) -> str:
    lines = ["# Contract Risk Report\n"]
    if not items:
        return "# Contract Risk Report\n\n_No clauses detected._"

    for i, item in enumerate(items, 1):
        risk = grade_item(item)
        lines.append(f"## {i}. {item['clause_type'].replace('_', ' ').title()}")
        lines.append(f"- **Risk Level:** {risk.upper()}")
        lines.append(f"- **Details:** {item.get('rationale','')}\n")
    return "\n".join(lines)

def save_report(text: str, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Report saved to {path}")
