# tools.py
class TextCleaner:
    """Helper to clean text"""
    def clean_text(self, text: str) -> str:
        return " ".join(text.split())
