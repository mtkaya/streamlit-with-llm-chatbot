from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Soru(BaseModel):
    soru: str
    model: str

@app.post("/sohbet")
async def sohbet(soru: Soru):
    command = ["ollama", "run", soru.model]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = proc.communicate(input=soru.soru)
    return {"yanit": output.strip()}
