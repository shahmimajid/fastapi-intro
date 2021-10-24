from fastapi import FastAPI

app = FastAPI(title="Fastapi-intro", version="0.0.1")


@app.get("/")
async def root():
    return {"message": "Hello World"}
