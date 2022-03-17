import itertools
import logging
from typing import List, Tuple

import tqdm

from modules.dict_service import inc_dict_counter


def count_ngrams(tokens: List[str]) -> Tuple[dict]:
    res, res_2, res_3 = {}, {}, {}
    for word, word_1, word_2 in zip(tokens, tokens[1:], tokens[2:]):
        inc_dict_counter(res, word)
        inc_dict_counter(res_2, (word, word_1))
        inc_dict_counter(res_3, (word, word_1, word_2))
    return res, res_2, res_3


def smooth(d1: dict, d2: dict, d3: dict):
    keys = list(d1.keys())
    for i, word_1 in tqdm.tqdm(enumerate(d1), total=len(keys)):
        for word_2 in keys[i:]:
            d2.update({(word_1, word_2): d2.get((word_1, word_2), 0) + 1})
    logging.info("Started smooth trigrams")
    for i, word_1 in tqdm.tqdm(enumerate(d1), total=len(keys)):
        for j, word_2 in enumerate(keys[i:], start=i):
            for word_3 in keys[j:]:
                d3.update({(word_1, word_2, word_3): d2.get((word_1, word_2, word_3), 0) + 1})


def count_perplection(prob: float, n: int):
    return (1 / prob) ** (1 / n)
