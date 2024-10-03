
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "3rd Oct"}

@app.get("/vit")
async def hello():
    return {"message": "Vit Demo"}