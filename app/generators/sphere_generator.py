from ..models.types import Point
from ..models.sphere_model import SphereModel
from .generator import Generator

class SphereGenerator(Generator):
    _radius: float
    _point1: Point
    _point2: Point
    _point3: Point

    def __init__(self, request_json: SphereModel):
        self._create_points(request_json)
        super().__init__(request_json)

    def _create_points(self, request_json: SphereModel):
        self._point1 = request_json.point
        self._point2 = request_json.point
        self._point3 = request_json.point

        self._point2.x += self._radius
        self._point3.x -= self._radius

        