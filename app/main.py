from fastapi import FastAPI
from .models.gmsh_model import GMSHModel
from .gmsh_generator import GMSHGenerator

app = FastAPI()

@app.get("/")
async def index(gmsh_data: GMSHModel):
    gmsh = GMSHGenerator(gmsh_data)
    gmsh.generate()
    mesh = gmsh.read_mesh_file()
    return mesh