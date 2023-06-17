from fastapi import FastAPI

from music.router import router

app = FastAPI()


app.include_router(
    router)
