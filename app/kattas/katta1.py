class Dictionary:
    def __init__(self):
        self._data = {}

    def newentry(self, word, definition):
        self._data[word] = definition
        return {"message": f"Entry added for {word}"}

    def look(self, word):
        return self._data.get(word, f"Can't find entry for {word}")


# instancia única (vive mientras la app esté arriba)
_dictionary = Dictionary()


def newentry(payload: dict):
    """
    payload esperado:
    {
        "word": "Apple",
        "definition": "A fruit that grows on trees"
    }
    """
    return _dictionary.newentry(
        payload["word"],
        payload["definition"]
    )


def look(payload: dict):
    """
    payload esperado:
    {
        "word": "Apple"
    }
    """
    return _dictionary.look(payload["word"])