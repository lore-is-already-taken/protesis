from typing import Dict, List
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


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
    data: List[Dict[str, str]]


@app.post("/data")
def data(recieve_data: hand_Data):
    # Process the incoming data
    print(recieve_data.data)
    return {"message": recieve_data}


def run_api():
    uvicorn.run(
        "app.api.api:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="debug",
    )
