import gmsh
from .models.gmsh_model import GMSHModel


class GMSHGenerator:
    def __init__(self, gmsh_data: GMSHModel):
        self.__gmsh = gmsh
        self.__gmsh_data = gmsh_data
        self.__mesh_size = gmsh_data.mesh_size

    def generate(self):
        title = self.__gmsh_data.title
        gmsh = self.__gmsh

        try:
            gmsh.initialize()

            gmsh.model.add(title)

            self.__add_points()
            self.__add_lines()
            self.__add_curve_loops()
            self.__add_plane_surfaces()

            gmsh.model.geo.synchronize()

            self.__add_physical_groups()

            gmsh.model.mesh.generate(self.__gmsh_data.dim)
            gmsh.write("app/meshs/" + title + ".msh")

            gmsh.fltk.run()

            gmsh.finalize()

        except Exception as e:
            print(e)

    def read_mesh_file(self):
        title = self.__gmsh_data.title

        with open("app/meshs/" + title + ".msh", "r") as file:
            mesh = file.read()
            return mesh

    def __add_points(self):
        points = self.__gmsh_data.points

        for point in points:
            self.__gmsh.model.geo.addPoint(
                point.x, point.y, point.z, self.__mesh_size, point.tag
            )

    def __add_lines(self):
        lines = self.__gmsh_data.lines

        for line in lines:
            self.__gmsh.model.geo.addLine(line.first_point, line.second_point, line.tag)

    def __add_curve_loops(self):
        curve_loops = self.__gmsh_data.curve_loops

        for curve_loop in curve_loops:
            self.__gmsh.model.geo.addCurveLoop(curve_loop.curve_loop, curve_loop.tag)

    def __add_plane_surfaces(self):
        plane_surfaces = self.__gmsh_data.plane_surfaces

        for plane_surface in plane_surfaces:
            self.__gmsh.model.geo.addPlaneSurface(
                plane_surface.plane_surface, plane_surface.tag
            )

    def __add_physical_groups(self):
        physical_groups = self.__gmsh_data.physical_groups

        for physical_group in physical_groups:
            self.__gmsh.model.geo.addPhysicalGroup(
                physical_group.dim, physical_group.tags, physical_group.tag
            )
