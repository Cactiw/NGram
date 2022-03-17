from typing import List, Tuple

from modules.dict_service import inc_dict_counter


def count_ngrams(tokens: List[str]) -> Tuple[dict]:
    res, res_2, res_3 = {}, {}, {}
    for word, word_1, word_2 in zip(tokens, tokens[1:], tokens[2:]):
        inc_dict_counter(res, word)
        inc_dict_counter(res_2, (word, word_1))
        inc_dict_counter(res_3, (word, word_1, word_2))
    return res, res_2, res_3


def count_perplection(prob: float, n: int):
    return (1 / prob) ** (1 / n)
