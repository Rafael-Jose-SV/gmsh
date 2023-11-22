import gmsh
from .models.gmsh_model import GMSHModel

class GMSHGenerator:
    def __init__(self, gmsh_data: GMSHModel):
        self._gmsh = gmsh
        self._gmsh_data = gmsh_data
        self._mesh_size = gmsh_data.mesh_size

    def generate(self):
        title = self._gmsh_data.title
        gmsh = self._gmsh

        try:
            gmsh.initialize()

            gmsh.model.add(title)

            self._add_points()
            self._add_lines()
            self._add_curve_loops()
            self._add_plane_surfaces()

            gmsh.model.geo.synchronize()

            self._add_physical_groups()

            gmsh.model.mesh.generate(self._gmsh_data.dim)
            gmsh.write("app/meshs/tmp.msh")

            # gmsh.fltk.run()

            gmsh.finalize()

        except Exception as e:
            print(e)

    def read_mesh_file(self):
        title = self._gmsh_data.title

        with open("app/mesh/tmp.msh", "r") as file:
            mesh = file.read()
            return mesh

    def _add_points(self):
        points = self._gmsh_data.points

        for point in points:
            self._gmsh.model.geo.addPoint(
                point.x, point.y, point.z, self._mesh_size, point.tag
            )

    def _add_lines(self):
        lines = self._gmsh_data.lines

        for line in lines:
            self._gmsh.model.geo.addLine(line.first_point, line.second_point, line.tag)

    def _add_curve_loops(self):
        curve_loops = self._gmsh_data.curve_loops

        for curve_loop in curve_loops:
            self._gmsh.model.geo.addCurveLoop(curve_loop.curve_loop, curve_loop.tag)

    def _add_plane_surfaces(self):
        plane_surfaces = self._gmsh_data.plane_surfaces

        for plane_surface in plane_surfaces:
            self._gmsh.model.geo.addPlaneSurface(
                plane_surface.plane_surface, plane_surface.tag
            )

    def _add_physical_groups(self):
        physical_groups = self._gmsh_data.physical_groups

        for physical_group in physical_groups:
            self._gmsh.model.geo.addPhysicalGroup(
                physical_group.dim, physical_group.tags, physical_group.tag
            )
