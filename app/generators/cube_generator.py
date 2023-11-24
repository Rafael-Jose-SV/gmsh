from ..models.types import Point
from ..models.cube_model import CubeModel
from .generator import Generator

class CubeGenerator(Generator):
    _point1: Point
    _point2: Point

    def __init__(self, request_json: CubeModel):
        self._create_points(request_json)
        super().__init__(request_json)

    def _create_points(self, request_json: CubeModel):
        self._point1 = request_json.point1
        self._point2 = request_json.point2
