from .types import *

class GMSHModel(BaseModel):
    mesh_size: float
    points: list[Point]
    lines: list[Line]
    curve_loops: list[CurveLoop]
    plane_surfaces: list[PlaneSurface]
    physical_groups: list[PhysicalGroup]
    dim: int