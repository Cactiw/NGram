import string
from typing import List

from nltk import word_tokenize


def tokenize(text) -> List[str]:
    return list(filter(
        lambda word: not any(map(lambda c: c in word, string.punctuation + "»«–“№…")),
        word_tokenize(text, language="russian")
    ))
