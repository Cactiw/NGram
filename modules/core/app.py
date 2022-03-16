from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import config

app = FastAPI()

origins = [
    f"http://localhost:{config.APP_PORT}", f"https://localhost:{config.APP_PORT}",
    "http://localhost:8080", "https://localhost:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "content-disposition"
    ]
)

