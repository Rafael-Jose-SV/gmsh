from pydantic import *
from typing import List
from .points import Points
from .lines import Lines
from .curve_loops import CurveLoops
from .plane_surfaces import PlaneSurfaces
from .physical_group import PhysicalGroup

class GMSHModel(BaseModel):
    title: str
    mesh_size: float
    points: List[Points]
    lines: List[Lines]
    curve_loops: List[CurveLoops]
    plane_surfaces: List[PlaneSurfaces]
    physical_groups: List[PhysicalGroup]
    dim: int