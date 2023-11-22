from pydantic import BaseModel
from typing import Optional

class Points(BaseModel):
    x: float
    y: float
    z: float
    tag: int

class Lines(BaseModel):
    first_point: int
    second_point: int
    tag: int

class CurveLoops(BaseModel):
    curve_loop: list[int]
    tag: int

class PlaneSurfaces(BaseModel):
    plane_surface: list[int]
    tag: int

class PhysicalGroup(BaseModel):
    dim: int
    tags: list[int]
    tag: int
    name: Optional[str] = None