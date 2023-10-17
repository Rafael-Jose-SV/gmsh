from fastapi import FastAPI
from .models import GMSHModel

app = FastAPI()

@app.get("/")
def index(gmsh_model: GMSHModel):
    return {}