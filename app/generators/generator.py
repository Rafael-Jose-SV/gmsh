import gmsh
from ..models.types import *

class Generator:
    _points: list[Point] = []
    _lines: list[Line] = []
    _curve_loops: list[CurveLoop] = []
    _plane_surfaces: list[PlaneSurface] = []
    _physical_groups: list[PhysicalGroup] = []

    def __init__(self, request_json):
        self._gmsh = gmsh

        self._points = request_json.points
        self._lines = request_json.lines
        self._curve_loops = request_json.curve_loops
        self._plane_surfaces = request_json.plane_surfaces
        self._physical_groups = request_json.physical_groups

    def generate(self):
        gmsh = self._gmsh

        try:
            gmsh.initialize()

            gmsh.model.add('tmp')

            self._add_points()
            self._add_lines()
            self._add_curve_loops()
            self._add_plane_surfaces()

            gmsh.model.geo.synchronize()

            self._add_physical_groups()

            gmsh.model.mesh.generate(self._gmsh_data.dim)
            gmsh.write("app/mesh/tmp.msh")

            gmsh.fltk.run()

            gmsh.finalize()

        except Exception as e:
            print(e)

    def read_mesh_file(self):
        with open("app/mesh/tmp.msh", "r") as file:
            mesh = file.read()
            return mesh

    def _add_points(self):
        for point in self._points:
            self._gmsh.model.geo.addPoint(
                point.x, point.y, point.z, self._gmsh_data._mesh_size, point.tag
            )

    def _add_lines(self):
        for line in self._lines:
            self._gmsh.model.geo.addLine(line.first_point, line.second_point, line.tag)

    def _add_curve_loops(self):
        for curve_loop in self._curve_loops:
            self._gmsh.model.geo.addCurveLoop(curve_loop.curve_loop, curve_loop.tag)

    def _add_plane_surfaces(self):
        for plane_surface in self._plane_surfaces:
            self._gmsh.model.geo.addPlaneSurface(
                plane_surface.plane_surface, plane_surface.tag
            )

    def _add_physical_groups(self):
        for physical_group in self._physical_groups:
            self._gmsh.model.geo.addPhysicalGroup(
                physical_group.dim, physical_group.tags, physical_group.tag
            )
