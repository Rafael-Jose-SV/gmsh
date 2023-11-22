from pydantic import *
from .types import *

class GMSHModel(BaseModel):
    title: str
    mesh_size: float
    points: list[Points]
    lines: list[Lines]
    curve_loops: list[CurveLoops]
    plane_surfaces: list[PlaneSurfaces]
    physical_groups: list[PhysicalGroup]
    dim: int