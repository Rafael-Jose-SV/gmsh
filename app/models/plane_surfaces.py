from pydantic import BaseModel
from typing import List

class PlaneSurfaces(BaseModel):
    plane_surface: List[int]
    tag: int