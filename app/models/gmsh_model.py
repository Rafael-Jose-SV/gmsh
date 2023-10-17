from pydantic import BaseModel
from typing import List
from points import Points
from lines import Lines
from curve_loops import CurveLoops
from plane_surfaces import PlaneSurfaces

class GMSHModel(BaseModel):
    title: str
    lc: float
    points: List[Points]
    lines: List[Lines]
    curve_loops: List[CurveLoops]
    plane_surfaces: List[PlaneSurfaces]
    dim: int
