from pydantic import BaseModel

class Lines(BaseModel):
    first_point: int
    second_point: int
    tag: int