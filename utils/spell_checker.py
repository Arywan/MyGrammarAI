from spellchecker import SpellChecker

spell = SpellChecker()

def correct_spelling(text):
    """Corrects spelling mistakes in the given text."""
    words = text.split()
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]
    return " ".join(corrected_words)
