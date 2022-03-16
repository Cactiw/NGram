
def inc_dict_counter(d: dict, key):
    d.update({key: d.get(key, 0) + 1})


def merge_dicts(d1: dict, d2: dict) -> dict:
    keys = list(d1)
    keys.extend(list(d2))
    keys = set(keys)

    return {k: d1.get(k, 0) + d2.get(k, 0) for k in keys}

