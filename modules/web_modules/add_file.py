import logging

from fastapi import UploadFile, File

from modules.core.app import app
from modules.dict_service import merge_dicts
from modules.ngram import count_ngrams
from modules.resources import Resources
from modules.tokenizer import tokenize


@app.post("/api/addFile")
async def add_file(file: UploadFile = File(...)):
    logging.info('Loading file...')
    text = (await file.read()).decode()
    tokens = tokenize(text)
    d, d2, d3 = count_ngrams(tokens)

    Resources.d_1 = merge_dicts(Resources.d_1, d)
    Resources.d_2 = merge_dicts(Resources.d_2, d2)
    Resources.d_3 = merge_dicts(Resources.d_3, d3)

    Resources.update_stats()
    logging.info('File added.')


@app.get("/api/countWords")
async def count_words() -> int:
    return sum(Resources.d_1.values())

