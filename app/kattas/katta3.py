
def build_word(payload: dict):
    """
    payload esperado:
    {
        "words": ["yoda", "best", "has"]
    }
    """
    words = payload.get("words", [])
    return "".join(word[i] for i, word in enumerate(words))