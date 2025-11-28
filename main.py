import os

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()




app.mount("/", StaticFiles(directory="ahmedayyad.dev", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 2200)),
    )