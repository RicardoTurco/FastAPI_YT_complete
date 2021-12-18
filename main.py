import uvicorn
from fastapi import FastAPI
from rotas import router


app = FastAPI()

app.include_router(router, prefix="")


if __name__ == "__main__":
    uvicorn.run(app)
