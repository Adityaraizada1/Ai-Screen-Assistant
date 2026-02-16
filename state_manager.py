BLOCKED_WORDS = ["exam", "final", "graded", "certification"]

def is_safe(text):
    text = text.lower()
    return not any(word in text for word in BLOCKED_WORDS)
