
from pydantic import BaseSettings


class Config(BaseSettings):
    APP_PORT: int = 22111


config = Config()
