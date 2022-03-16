
import nltk
import uvicorn

from config import config

import modules.web_modules.add_file


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

