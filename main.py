import os

import nltk
import uvicorn
import logging

from fastapi import Request
from fastapi.responses import FileResponse

from config import config

import modules.web_modules.add_file
import modules.web_modules.word_service
from modules.core.app import app

logging.basicConfig(level=logging.INFO)


def check_install():
    nltk.download('punkt')


web_root = "dist/"


@app.get("/", response_class=FileResponse)
def read_index(request: Request):
    path = f'{web_root}index.html'
    return FileResponse(path)


@app.get("/{catchall:path}", response_class=FileResponse)
def read_index(request: Request):
    # check first if requested file exists
    path = request.path_params["catchall"]
    file = web_root + path

    # logging.info(f'look for: {path}, {file}')
    if os.path.exists(file):
        # logging.info("File found!")
        return FileResponse(file)
        # return templates.TemplateResponse(template, context, media_type='text/html')

    # otherwise return index files
    index = f"{web_root}index.html"
    return FileResponse(index)



def start_app():
    uvicorn.run(
        "modules.core.app:app",
        host="0.0.0.0",
        port=config.APP_PORT,
        log_level="info"
    )


if __name__ == "__main__":
    check_install()
    start_app()

