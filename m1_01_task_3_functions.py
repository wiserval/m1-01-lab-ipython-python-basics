def to_float(value):
    """Converts a string to a float, returns None if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def clean_string(text):
    """Removes whitespace and makes casing consistent."""
    if isinstance(text, str):
        return text.strip().lower()
    return None