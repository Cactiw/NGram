from modules.core.app import app
from modules.resources import Resources


@app.get("/api/getAutocomplete")
async def get_autocomplete(start_string: str):
    words = start_string.split()[:3]
    suitable = []
    if len(words) >= 3:
        # Фраза длинная
        suitable.extend(list(filter(lambda x, y: x[0] == words[0] and x[1] == words[1] and x[2].startswith(words[2]), Resources.d_3_stats.items())))
    if len(words) >= 2:
        suitable.extend(list(filter(lambda x, y: x[0] == words[0] and x[1].startswith(words[1]), Resources.d_2_stats.items())))
    if len(words) >= 1:
        suitable.extend(list(filter(lambda x, y: x[0].startswith(words[0]), Resources.d_1_stats.items())))
    return sorted(suitable, key=lambda x, y: y, reverse=True)[:10]

