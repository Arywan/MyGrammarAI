import re

def clean_text(text):
    """Removes extra spaces and special characters from the text."""
    text = text.strip()  # Remove leading and trailing spaces
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text
