from typing import Union
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"World from : {os.environ.get('ENV', 'DEFAULT')}"}