from fastapi import FastAPI
from generator import generate_event 


app = FastAPI()

@app.get("/event")
def get_event():
    """Returns a single synthetic event"""
    return generate_event()

