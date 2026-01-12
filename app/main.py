from fastapi import FastAPI
from app.kattas import katta1, katta2, katta3
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "version": os.getenv("APP_VERSION", "dev"),
        "client": os.getenv("CLIENT_NAME", "local")
    }

@app.post("/kata/one/add")
def run_kata_one_add(payload: dict):
    return {"result": katta1.newentry(payload)}

@app.post("/kata/one/look")
def run_kata_one_lookUp(payload: dict):
    return {"result": katta1.look(payload)}

@app.post("/kata/two")
def run_kata_two(payload: dict):
    return {"result": katta2.get_total(payload)}

@app.post("/kata/three")
def run_kata_three(payload: dict):
    return {"result": katta3.build_word(payload)}
