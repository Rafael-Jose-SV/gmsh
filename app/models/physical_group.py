from pydantic import BaseModel
from typing import List, Optional

class PhysicalGroup(BaseModel):
    dim: int
    tags: List[int]
    tag: int
    name: Optional[str] = None