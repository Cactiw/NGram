from modules.core.app import app
from modules.resources import Resources


@app.get("/api/getAutocomplete")
async def get_autocomplete(start_string: str):
    words = start_string.split()[-3:]
    if start_string.endswith(' '):
        words = words[-2:] + ['']
    print(words)
    suitable = []
    if len(words) >= 3:
        # Фраза длинная
        suitable.extend(list(filter(lambda x_y: x_y[0][0] == words[0] and x_y[0][1] == words[1] and x_y[0][2].startswith(words[2]), Resources.d_3_stats.items())))
    if not suitable and len(words) >= 2:
        suitable.extend(list(filter(lambda x_y: x_y[0][0] == words[0] and x_y[0][1].startswith(words[1]), Resources.d_2_stats.items())))
    if not suitable and len(words) >= 1:
        suitable.extend(list(map(lambda word_y: ((word_y[0],), word_y[1]),
                                 filter(lambda x_y: x_y[0].startswith(words[0]), Resources.d_1_stats.items()))))
    print(suitable)
    return sorted(suitable, key=lambda x_y: x_y[1], reverse=True)[:7]


@app.get("/api/spellcheck")
async def spellcheck(q: str):
    tokens = q.split()
    suitable = []
    for words in zip(tokens, tokens[1:], tokens[2:]):
        suitable = list(filter(lambda x_y: x_y[0][0] == words[0] and x_y[0][2] == words[2], Resources.d_3_stats.items()))
        return sorted(suitable, key=lambda words_y: words_y[1], reverse=True)[:7]

