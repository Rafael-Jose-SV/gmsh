from pydantic import BaseModel
from typing import List, Optional

class PhysicalGroup(BaseModel):
    dim: int
    lines: List[int]
    tag: int
    name: Optional[str]