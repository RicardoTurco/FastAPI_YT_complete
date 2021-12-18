import uvicorn
from fastapi import FastAPI
from models.papel import Papel


app = FastAPI()

banco_de_dados = []


@app.post("/papeis")
def add_item(item: Papel):
    banco_de_dados.append(item)
    return item


@app.get("/papeis")
def list_item():
    return banco_de_dados


if __name__ == "__main__":
    uvicorn.run(app)
