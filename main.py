import os

import uvicorn
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return 'ok'


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 2200)),
    )