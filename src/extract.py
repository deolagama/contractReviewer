from typing import List, Dict
from .keywords import CLAUSE_KEYWORDS

def detect_clauses(chunks: List[str]) -> List[Dict]:
    """Simple keyword-based clause detection."""
    results = []
    for chunk in chunks:
        for ctype, kws in CLAUSE_KEYWORDS.items():
            if any(kw.lower() in chunk.lower() for kw in kws):
                results.append({
                    "clause_type": ctype,
                    "rationale": chunk[:200] + "..." if len(chunk) > 200 else chunk,
                    "key_numbers": {},  # Could parse numbers later
                })
    return results
