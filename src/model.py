# src/model.py
from transformers import pipeline

class TinyExtractor:
    """Use a small LLM for simple information extraction."""
    def __init__(self):
        self.pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def classify_clause(self, text: str):
        # This is placeholder logic; fine-tune later
        result = self.pipe(text[:512])[0]
        return {"label": result["label"], "score": result["score"]}
