from fastapi import FastAPI
from pydantic import BaseModel 
import transformers
import torch
from typing import List

import csv # Allows us to read and write csv files
from pprint import pprint # Make our print functions easier to read

from transformers import pipeline
# pipe = pipeline(model="model/t5-small")
pipe = pipeline(model="t5-small")


class TextToTranslate(BaseModel):
    input_text: str

class TextsToTranslate(BaseModel):
    input_list: List[str]
    
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"} 
    
@app.get("/ping")
def cool_stuff():
    return {"message": "pong"}
    
@app.get("/messy")
def cool_stuff():
    return {"message": "This is incredibly neat"}

# @app.post("/echo")
# def echo(message: str):
#     return {"echo": message}
    
@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}
    
@app.post("/translate1")
def translate1(text_to_translate: TextToTranslate):
    return {"message": pipe(text_to_translate.input_text)}
    
@app.post("/translatebatch")
def translatebatch(list_to_translate: TextsToTranslate):
    return {"message": pipe(list_to_translate.input_list)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)