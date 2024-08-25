from typing import Dict, List
import json
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.api.hand_move import hand_handler


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class hand_Data(BaseModel):
    # data: List[Dict[str, str]]
    # data: List[str]
    data: str


# @app.post("/data")
# def data(recieve_data: hand_Data):
@app.get("/data")
def data():
    # @app.get("/data")
    # def data():
    # Process the incoming data
    data = """[
    {"engine": "upper_thumb", "value": 0},
    {"engine": "lower_thumb", "value": 0},
    {"engine": "index_finger", "value": 0},
    {"engine": "middle_finger", "value": 0},
    {"engine": "ring_finger", "value": 0}
    ]"""
    # hand_handler(json.loads(recieve_data.data))
    hand_handler(json.loads(data))
    return {"message": data}


def run_api():
    uvicorn.run(
        "app.api.api:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="debug",
    )
