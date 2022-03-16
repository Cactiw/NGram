
import nltk
import uvicorn
import logging

from config import config

import modules.web_modules.add_file
import modules.web_modules.word_service

logging.basicConfig(level=logging.INFO)


def check_install():
    nltk.download('punkt')


def start_app():
    uvicorn.run(
        "modules.core.app:app",
        host="localhost",
        port=config.APP_PORT,
        log_level="info"
    )


if __name__ == "__main__":
    check_install()
    start_app()

