from fastapi import FastAPI
from .models.gmsh_model import GMSHModel
from .generators.generator import Generator

app = FastAPI()

@app.get("/")
async def index(gmsh_data: GMSHModel):
    gmsh = Generator(gmsh_data)
    gmsh.generate()
    mesh = gmsh.read_mesh_file()
    return mesh