from pydantic import BaseModel
from typing import List

class CurveLoops(BaseModel):
    curve_loop: List
    tag: 1