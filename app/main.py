from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Fastapi-intro", version="0.0.1")


@app.get("/")
async def home():
    data = {"text": "hi"}
    return {"data": data}


@app.get("/page/{page_name}")
async def page(page_name: str):
    data = {"page": page_name}
    return {"data": data}
