from fastapi import FastAPI
from stockanalysis.trending import get_trending

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/trending")
async def get_trending_stocks():
    metadata, data = get_trending()
    return {
        "metadata": metadata,
        "data": data
    }