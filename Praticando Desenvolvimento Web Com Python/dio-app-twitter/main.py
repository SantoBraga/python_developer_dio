from fastapi import FastAPI
from src.responses import TrendItem
from src.services import *

app = FastAPI()


@app.get("/trends", response_model=list[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


if __name__ == '__main__':

    save_trends()  # Init DB

    # Run server (Terminal) -> uvicorn main:app --reload
