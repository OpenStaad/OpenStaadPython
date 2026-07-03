"""
geometry.py — dominio Geometry del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code`; los guards de validación de entrada que en el
oficial lanzaban se convierten en early-return. Se conservan los condicionales
que son lógica de retorno (return [], return bool, etc.).
"""

from .bridge import Bridge
from ._com import acquire


class Geometry:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._geometry = staad.Geometry

        self._functions = [
            "CreateNode", "CreateBeam", "CreatePlate", "CreateSolid", "AddNode",
            "AddBeam", "AddPlate", "AddSolid", "AddMultipleNodes", "AddMultipleBeams",
            "AddMultiplePlates", "AddMultipleSolids", "DeleteNode", "DeleteBeam",
            "DeletePlate", "DeleteSolid", "SplitBeam", "SplitBeamInEqlParts",
            "GetLastNodeNo", "GetLastBeamNo", "GetLastPlateNo", "GetLastSolidNo",
            "GetNoOfSelectedNodes", "GetSelectedNodes", "GetNoOfSelectedBeams",
            "GetSelectedBeams", "GetNoOfSelectedPlates", "GetSelectedPlates",
            "GetNoOfSelectedSolids", "GetSelectedSolids", "GetNodeCoordinates",
            "GetNodeNumber", "GetNodeDistance", "GetBeamLength", "SelectMultipleNodes",
            "SelectMultipleBeams", "SelectMultiplePlates", "SelectMultipleSolids",
            "SelectNode", "SelectBeam", "SelectPlate", "SelectSolid", "GetNodeCount",
            "GetMemberCount", "GetPlateCount", "GetSolidCount", "GetNodeList",
            "GetBeamList", "GetPlateList", "GetSolidList", "GetNodeIncidence",
            "GetMemberIncidence", "GetPlateIncidence", "GetSolidIncidence", "CreateGroup",
            "ClearNodeSelection", "ClearMemberSelection", "ClearPlateSelection",
            "ClearSolidSelection", "SetNodeUniqueID", "SetMemberUniqueID",
            "SetPlateUniqueID", "SetSolidUniqueID", "SetNodeCoordinate",
            "DoTranslationalRepeat", "GetNodeUniqueID", "GetMemberUniqueID",
            "GetPlateUniqueID", "GetSolidUniqueID", "GetPlateNodeCount",
            "GetNoOfGeneratedQuadPanels", "GetGeneratedQuadPanelIncidences", "IsZUp",
            "IsBeam", "IsColumn", "GetNoOfBeamsConnectedAtNode", "GetBeamsConnectedAtNode",
            "RenumberBeam", "IsOrphanNode", "GetGroupCountAll", "GetGroupCount",
            "GetGroupNames", "GetGroupEntityCount", "GetGroupEntities", "CreateGroupEx",
            "DeleteGroup", "UpdateGroup", "DefineParametricSurface",
            "AddParametricSurfaceToModel", "CommitParametricSurfaceMesh",
            "RemoveParametricSurfaceMesh", "AddDensityPointToSurface",
            "AddDensityLineToSurface", "AddCircularRegionToSurface",
            "AddPolygonalRegionToSurface", "GetParametricSurfaceCount",
            "GetParametricSurfaceInfo", "GetParametricSurfaceMeshInfo",
            "GetParametricSurfaceMeshData", "SetParametricSurfaceUniqueID",
            "GetParametricSurfaceUniqueID", "GetAreaOfPlates", "CreateMultiplePlates",
            "SetParametricSurfaceSubType", "GetParametricSurfaceSubType",
            "SetCheckForIdenticalEntity", "CreateMultipleNodes", "CreateMultipleBeams",
            "GetParametricSurfaceInfoEx", "IntersectBeams", "MergeBeams", "MergeNodes",
            "GetCountOfBreakableBeamsAtSpecificNodes", "BreakBeamsAtSpecificNodes",
            "GetIntersectBeamsCount", "ClearPhysicalMemberSelection",
            "CreatePhysicalMember", "DeletePhysicalMember",
            "GetAnalyticalMemberCountForPhysicalMember",
            "GetAnalyticalMembersForPhysicalMember", "GetLastPhysicalMemberNo",
            "GetNoOfSelectedPhysicalMembers", "GetSelectedPhysicalMembers",
            "GetPhysicalMemberCount", "GetPhysicalMemberList", "GetPhysicalMemberUniqueID",
            "GetPMemberCount", "SelectMultiplePhysicalMembers", "SelectPhysicalMember",
            "SetPhysicalMemberUniqueID", "SetPID", "GetPID", "GetFlagForHiddenEntities",
            "GetMemberIncidence_CIS2", "GetNodeIncidence_CIS2", "GetPlateIncidence_CIS2",
            "GetSolidIncidence_CIS2", "SetFlagForHiddenEntities",
        ]
        for function_name in self._functions:
            self._geometry._FlagAsMethod(function_name)

    # ------------------------------------------------------------------ #
    # Nodos
    # ------------------------------------------------------------------ #
    def CreateNode(self, nNodeNo: int, x: float, y: float, z: float):
        self._geometry.CreateNode(
            self._b.in_value(nNodeNo), self._b.in_value(x),
            self._b.in_value(y), self._b.in_value(z)
        )

    def AddNode(self, x: float, y: float, z: float):
        return self._geometry.AddNode(x, y, z)

    def DeleteNode(self, nNodeNo: int):
        self._geometry.DeleteNode(self._b.in_value(nNodeNo))

    def GetNodeCount(self):
        return self._geometry.GetNodeCount()

    def GetLastNodeNo(self):
        return self._geometry.GetLastNodeNo()

    def GetNodeCoordinates(self, node: int):
        x = self._b.out_double()
        y = self._b.out_double()
        z = self._b.out_double()
        self._geometry.GetNodeCoordinates(node, x.ref, y.ref, z.ref)
        return (x.value, y.value, z.value)

    def GetNodeNumber(self, x_y_z_coordinates: tuple):
        return self._geometry.GetNodeNumber(x_y_z_coordinates[0], x_y_z_coordinates[1], x_y_z_coordinates[2])

    def GetNodeDistance(self, nodeA, nodeB):
        return self._geometry.GetNodeDistance(nodeA, nodeB)

    def GetNodeIncidence(self, node):
        x = self._b.out_double()
        y = self._b.out_double()
        z = self._b.out_double()
        self._geometry.GetNodeIncidence(node, x.ref, y.ref, z.ref)
        return (x.value, y.value, z.value)

    def GetNodeList(self):
        n = int(self._geometry.GetNodeCount())
        if n <= 0:
            return []
        nodes = self._b.out_int_array(n)
        self._geometry.GetNodeList(nodes.ref)
        return nodes.value

    def GetNodeUniqueID(self, nodeNo: int):
        return self._geometry.GetNodeUniqueID(nodeNo)

    def SetNodeUniqueID(self, nodeNo: int, uniqueID: str):
        self._geometry.SetNodeUniqueID(nodeNo, uniqueID)

    def SetNodeCoordinate(self, nodeNo: int, x: float, y: float, z: float):
        self._geometry.SetNodeCoordinate(nodeNo, x, y, z)

    def SelectNode(self, nodeID):
        return bool(self._geometry.SelectNode(nodeID))

    def GetNoOfSelectedNodes(self):
        return self._geometry.GetNoOfSelectedNodes()

    def GetSelectedNodes(self):
        n = self.GetNoOfSelectedNodes()
        nodes = self._b.out_int_array(n)
        self._geometry.GetSelectedNodes(nodes.ref)
        return nodes.value

    def SelectMultipleNodes(self, nodes: list):
        return bool(self._geometry.SelectMultipleNodes(self._b.in_int_array(nodes)))

    def ClearNodeSelection(self):
        self._geometry.ClearNodeSelection()

    def IsOrphanNode(self, nodeNo: int):
        return bool(self._geometry.IsOrphanNode(nodeNo))

    def AddMultipleNodes(self, coordinates):
        if (not isinstance(coordinates, list)
                or not all(isinstance(node, list) for node in coordinates)
                or not all(all(isinstance(c, (float, int)) for c in node) for node in coordinates)):
            return
        if not all(len(lst) == 3 for lst in coordinates):
            return
        return [self.AddNode(x, y, z) for x, y, z in coordinates]

    def CreateMultipleNodes(self, node_ids: list, nodeCoordinates: list):
        if len(node_ids) != len(nodeCoordinates):
            return
        for i, coords in enumerate(nodeCoordinates):
            if len(coords) != 3:
                return
            x, y, z = coords
            self.CreateNode(node_ids[i], x, y, z)

    # ------------------------------------------------------------------ #
    # Vigas / miembros
    # ------------------------------------------------------------------ #
    def CreateBeam(self, nBeamNo: int, nNodeStart: int, nNodeEnd: int):
        self._geometry.CreateBeam(
            self._b.in_value(nBeamNo), self._b.in_value(nNodeStart), self._b.in_value(nNodeEnd)
        )

    def AddBeam(self, nNodeStart: int, nNodeEnd: int):
        return self._geometry.AddBeam(self._b.in_value(nNodeStart), self._b.in_value(nNodeEnd))

    def DeleteBeam(self, BeamNo: int):
        self._geometry.DeleteBeam(self._b.in_value(BeamNo))

    def GetMemberCount(self):
        return self._geometry.GetMemberCount()

    def GetLastBeamNo(self):
        return self._geometry.GetLastBeamNo()

    def GetBeamLength(self, beam: int):
        return self._geometry.GetBeamLength(beam)

    def GetBeamList(self):
        n = self._geometry.GetMemberCount()
        if n <= 0:
            return []
        beams = self._b.out_int_array(n)
        self._geometry.GetBeamList(beams.ref)
        return beams.value

    def GetMemberIncidence(self, beam):
        a = self._b.out_int()
        b = self._b.out_int()
        self._geometry.GetMemberIncidence(beam, a.ref, b.ref)
        return (a.value, b.value)

    def SelectBeam(self, beamID):
        return bool(self._geometry.SelectBeam(beamID))

    def SelectMultipleBeams(self, beam_ids: list):
        self._geometry.SelectMultipleBeams(self._b.in_int_array_variant(beam_ids).ref)

    def GetNoOfSelectedBeams(self):
        return self._geometry.GetNoOfSelectedBeams()

    def GetSelectedBeams(self):
        n = self._geometry.GetNoOfSelectedBeams()
        beams = self._b.out_int_array(n)
        self._geometry.GetSelectedBeams(beams.ref)
        return beams.value

    def ClearMemberSelection(self):
        self._geometry.ClearMemberSelection()

    def GetNoOfBeamsConnectedAtNode(self, node):
        return self._geometry.GetNoOfBeamsConnectedAtNode(node)

    def GetBeamsConnectedAtNode(self, node):
        n = self.GetNoOfBeamsConnectedAtNode(node)
        beams = self._b.out_int_array(n)
        self._geometry.GetBeamsConnectedAtNode(node, beams.ref)
        return beams.value

    def RenumberBeam(self, oldBeamNo: int, newBeamNo: int):
        return bool(int(self._geometry.RenumberBeam(oldBeamNo, newBeamNo)))

    def IsBeam(self, beam_no: int, tol_angle: float):
        return bool(int(self._geometry.IsBeam(beam_no, tol_angle)))

    def IsColumn(self, column_no: int, tol_angle: float):
        return bool(int(self._geometry.IsColumn(column_no, tol_angle)))

    def SplitBeam(self, beamNo: int, nodes: int, distToNodes: list):
        self._geometry.SplitBeam(beamNo, nodes, self._b.in_double_array(distToNodes))

    def SplitBeamInEqlParts(self, nBeamNo: int, nParts: int):
        self._geometry.SplitBeamInEqlParts(nBeamNo, nParts)

    def SetMemberUniqueID(self, beamNo: int, uniqueID: str):
        self._geometry.SetMemberUniqueID(beamNo, uniqueID)

    def GetMemberUniqueID(self, memberNo: int):
        return self._geometry.GetMemberUniqueID(memberNo)

    def AddMultipleBeams(self, incidences):
        if (not isinstance(incidences, list)
                or not all(isinstance(beam, list) for beam in incidences)
                or not all(all(isinstance(n, int) for n in beam) for beam in incidences)):
            return
        if not all(len(lst) == 2 for lst in incidences):
            return
        return [self.AddBeam(s, e) for s, e in incidences]

    def CreateMultipleBeams(self, beam_ids: list, beam_incidences: list):
        if len(beam_ids) != len(beam_incidences):
            return
        for i, incidence in enumerate(beam_incidences):
            if len(incidence) != 2:
                return
            start_node, end_node = incidence
            self.CreateBeam(beam_ids[i], start_node, end_node)

    # ------------------------------------------------------------------ #
    # Placas
    # ------------------------------------------------------------------ #
    def CreatePlate(self, nPlateNo: int, nNodeA: int, nNodeB: int, nNodeC: int, nNodeD: int = 0):
        self._geometry.CreatePlate(
            self._b.in_value(nPlateNo), self._b.in_value(nNodeA), self._b.in_value(nNodeB),
            self._b.in_value(nNodeC), self._b.in_value(nNodeD)
        )

    def AddPlate(self, nNodeA: int, nNodeB: int, nNodeC: int, nNodeD: int = 0):
        return self._geometry.AddPlate(
            self._b.in_value(nNodeA), self._b.in_value(nNodeB),
            self._b.in_value(nNodeC), self._b.in_value(nNodeD)
        )

    def DeletePlate(self, nPlateNo: int):
        self._geometry.DeletePlate(self._b.in_value(nPlateNo))

    def GetPlateCount(self):
        return int(self._geometry.GetPlateCount())

    def GetLastPlateNo(self):
        return self._geometry.GetLastPlateNo()

    def GetPlateList(self):
        n = int(self._geometry.GetPlateCount())
        if n <= 0:
            return []
        plates = self._b.out_int_array(n)
        self._geometry.GetPlateList(plates.ref)
        return plates.value

    def GetPlateIncidence(self, plateNo: int):
        a = self._b.out_int()
        b = self._b.out_int()
        c = self._b.out_int()
        d = self._b.out_int()
        self._geometry.GetPlateIncidence(plateNo, a.ref, b.ref, c.ref, d.ref)
        return (a.value, b.value, c.value, d.value)

    def GetPlateNodeCount(self, plateNo: int):
        return self._geometry.GetPlateNodeCount(plateNo)

    def SelectPlate(self, nPlateNo: int):
        if nPlateNo not in self.GetPlateList():
            return False
        return bool(self._geometry.SelectPlate(self._b.in_value(nPlateNo)))

    def GetNoOfSelectedPlates(self):
        return int(self._geometry.GetNoOfSelectedPlates())

    def GetSelectedPlates(self, isSorted: bool = False):
        n = self.GetNoOfSelectedPlates()
        plates = self._b.out_int_array(n)
        self._geometry.GetSelectedPlates(plates.ref, isSorted)
        return plates.value

    def SelectMultiplePlates(self, plates: list):
        return bool(self._geometry.SelectMultiplePlates(self._b.in_int_array(plates)))

    def ClearPlateSelection(self):
        self._geometry.ClearPlateSelection()

    def SetPlateUniqueID(self, plateNo: int, uniqueID: str):
        self._geometry.SetPlateUniqueID(plateNo, uniqueID)

    def GetPlateUniqueID(self, plateNo: int):
        return self._geometry.GetPlateUniqueID(plateNo)

    def GetAreaOfPlates(self, plateList):
        if len(plateList) == 0:
            return []
        vt_plateList = self._b.in_int_array(plateList)
        areas = self._b.out_double_array(len(plateList))
        self._geometry.GetAreaOfPlates(vt_plateList, areas.ref)
        return areas.value

    def AddMultiplePlates(self, incidences):
        if (not isinstance(incidences, list)
                or not all(isinstance(row, list) for row in incidences)
                or not all(all(isinstance(n, int) for n in row) for row in incidences)):
            return
        if not all(len(lst) in (4, 3) for lst in incidences):
            return
        plate_ids = []
        for incidence in incidences:
            if len(incidence) == 3:
                incidence.append(0)
            a, b, c, d = incidence
            plate_ids.append(self.AddPlate(a, b, c, d))
        return plate_ids

    def CreateMultiplePlates(self, plate_ids, plate_incidences: list):
        if isinstance(plate_ids, int):
            plate_ids = [plate_ids]
        if len(plate_ids) != len(plate_incidences):
            return
        if (not all(isinstance(row, list) for row in plate_incidences)
                or not all(all(isinstance(n, int) for n in row) for row in plate_incidences)):
            return
        if not all(len(lst) in (4, 3) for lst in plate_incidences):
            return
        for i, incidence in enumerate(plate_incidences):
            if len(incidence) == 3:
                incidence.append(0)
            a, b, c, d = incidence
            self.CreatePlate(plate_ids[i], a, b, c, d)

    # ------------------------------------------------------------------ #
    # Sólidos
    # ------------------------------------------------------------------ #
    def CreateSolid(self, solidNo: int, nodeA: int, nodeB: int, nodeC: int, nodeD: int, nodeE: int, nodeF: int, nodeG: int = 0, nodeH: int = 0):
        self._geometry.CreateSolid(solidNo, nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH)

    def AddSolid(self, nodeA: int, nodeB: int, nodeC: int, nodeD: int, nodeE: int, nodeF: int, nodeG: int = 0, nodeH: int = 0):
        return self._geometry.AddSolid(nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH)

    def DeleteSolid(self, solidID):
        self._geometry.DeleteSolid(solidID)

    def GetSolidCount(self):
        return int(self._geometry.GetSolidCount())

    def GetLastSolidNo(self):
        return int(self._geometry.GetLastSolidNo())

    def GetSolidList(self):
        n = int(self._geometry.GetSolidCount())
        if n <= 0:
            return []
        solids = self._b.out_int_array(n)
        self._geometry.GetSolidList(solids.ref)
        return solids.value

    def GetSolidIncidence(self, solidNo):
        outs = [self._b.out_int() for _ in range(8)]
        self._geometry.GetSolidIncidence(solidNo, *[o.ref for o in outs])
        return tuple(o.value for o in outs)

    def SelectSolid(self, solidID):
        return bool(self._geometry.SelectSolid(solidID))

    def GetNoOfSelectedSolids(self):
        return int(self._geometry.GetNoOfSelectedSolids())

    def GetSelectedSolids(self, isSorted: bool = False):
        n = self.GetNoOfSelectedSolids()
        solids = self._b.out_int_array(n)
        self._geometry.GetSelectedSolids(solids.ref, isSorted)
        return solids.value

    def SelectMultipleSolids(self, solids: list):
        return bool(self._geometry.SelectMultipleSolids(self._b.in_int_array(solids)))

    def ClearSolidSelection(self):
        self._geometry.ClearSolidSelection()

    def SetSolidUniqueID(self, solidNo: int, uniqueID: str):
        self._geometry.SetSolidUniqueID(solidNo, uniqueID)

    def GetSolidUniqueID(self, solidNo: int):
        return self._geometry.GetSolidUniqueID(solidNo)

    def AddMultipleSolids(self, incidences):
        if (not isinstance(incidences, list)
                or not all(isinstance(row, list) for row in incidences)
                or not all(all(isinstance(n, int) for n in row) for row in incidences)):
            return
        if not all(len(lst) in (8, 7, 6) for lst in incidences):
            return
        solid_ids = []
        for incidence in incidences:
            if len(incidence) == 6:
                incidence.extend([0, 0])
            elif len(incidence) == 7:
                incidence.append(0)
            a, b, c, d, e, f, g, h = incidence
            solid_ids.append(self.AddSolid(a, b, c, d, e, f, g, h))
        return solid_ids

    # ------------------------------------------------------------------ #
    # Grupos
    # ------------------------------------------------------------------ #
    def CreateGroup(self, group_type: int, group_name: str):
        self._geometry.CreateGroup(group_type, group_name)

    def CreateGroupEx(self, groupType: int, groupName: str, entityList: list):
        size = len(entityList)
        if size == 0:
            return
        self._geometry.CreateGroupEx(groupType, groupName, size, self._b.in_int_array(entityList))

    def GetGroupCount(self, grouptype):
        return self._geometry.GetGroupCount(grouptype)

    def GetGroupCountAll(self):
        return self._geometry.GetGroupCountAll()

    def GetGroupNames(self, grouptype):
        n = self._geometry.GetGroupCount(grouptype)
        names = self._b.out_str_array(n)
        self._geometry.GetGroupNames(grouptype, names.ref)
        return names.value

    def GetGroupEntityCount(self, group_name):
        return self._geometry.GetGroupEntityCount(group_name)

    def GetGroupEntities(self, group_name):
        n = self._geometry.GetGroupEntityCount(group_name)
        entities = self._b.out_int_array(n)
        self._geometry.GetGroupEntities(group_name, entities.ref)
        return entities.value

    def DeleteGroup(self, groupName: str):
        self._geometry.DeleteGroup(groupName)

    def UpdateGroup(self, groupName: str, update_option: int, entityList: list):
        self._geometry.UpdateGroup(groupName, update_option, len(entityList), self._b.in_int_array(entityList))

    # ------------------------------------------------------------------ #
    # Repetición / transformaciones
    # ------------------------------------------------------------------ #
    def DoTranslationalRepeat(self, link_bays: bool, open_base: bool, axis_dir: int, spacing_list: list, no_of_bays: int, renumber_bays: bool, renumber_list: list, geometry_only_flag: bool):
        renumber = self._b.in_int_array(renumber_list) if renumber_bays else None
        spacing = self._b.in_double_array(spacing_list)
        result = self._geometry.DoTranslationalRepeat(
            int(link_bays), int(open_base), axis_dir, spacing, no_of_bays,
            int(renumber_bays), renumber, int(geometry_only_flag)
        )
        return bool(result)

    # ------------------------------------------------------------------ #
    # Quad panels / hidden / misc
    # ------------------------------------------------------------------ #
    def GetNoOfGeneratedQuadPanels(self):
        return self._geometry.GetNoOfGeneratedQuadPanels()

    def GetGeneratedQuadPanelIncidences(self):
        size = self.GetNoOfGeneratedQuadPanels()
        if size <= 0:
            return [[], [], [], []]
        cols = [self._b.out_int_array(size) for _ in range(4)]
        self._geometry.GetGeneratedQuadPanelIncidences(*[c.ref for c in cols])
        return [c.value for c in cols]

    def IsZUp(self):
        return bool(self._geometry.IsZUp())

    def SetPID(self, EntityNo: int, EntityType: int, PropertyID: int):
        self._geometry.SetPID(EntityNo, EntityType, PropertyID)

    def GetPID(self, EntityNo: int, EntityType: int):
        return int(self._geometry.GetPID(EntityNo, EntityType))

    def GetFlagForHiddenEntities(self):
        return int(self._geometry.GetFlagForHiddenEntities())

    def SetFlagForHiddenEntities(self, flag: int):
        if flag not in (0, 1, 2):
            return
        self._geometry.SetFlagForHiddenEntities(flag)

    def SetCheckForIdenticalEntity(self, entityType: int, checkFlag: bool):
        if entityType not in (1, 2, 3, 4, 5):
            return None
        return bool(self._geometry.SetCheckForIdenticalEntity(entityType, int(checkFlag)))

    # ------------------------------------------------------------------ #
    # Superficies paramétricas
    # ------------------------------------------------------------------ #
    def DefineParametricSurface(self, name: str, type: int, origin_Node: int, x_vertex_node: int, y_vertex_node: int, vertices_list: list, auto_generate: bool):
        return self._geometry.DefineParametricSurface(
            name, type, origin_Node, x_vertex_node, y_vertex_node,
            len(vertices_list), self._b.in_int_array(vertices_list), int(auto_generate)
        )

    def AddParametricSurfaceToModel(self, surfaceNo: int):
        return bool(self._geometry.AddParametricSurfaceToModel(surfaceNo))

    def CommitParametricSurfaceMesh(self, surfaceNo: int):
        return bool(self._geometry.CommitParametricSurfaceMesh(surfaceNo))

    def RemoveParametricSurfaceMesh(self, surfaceNo: int):
        return bool(self._geometry.RemoveParametricSurfaceMesh(surfaceNo))

    def AddDensityPointToSurface(self, surfaceNo: int, pointData):
        self._geometry.AddDensityPointToSurface(surfaceNo, pointData)

    def AddDensityLineToSurface(self, surfaceNo: int, x1: float, y1: float, z1: float, density1: int, x2: float, y2: float, z2: float, density2: int, divisions: int):
        return self._geometry.AddDensityLineToSurface(surfaceNo, x1, y1, z1, density1, x2, y2, z2, density2, divisions)

    def AddCircularRegionToSurface(self, surfaceNo: int, x: float, y: float, z: float, radius: float, divisions: int, density: int, is_opening: bool = False):
        return bool(self._geometry.AddCircularRegionToSurface(surfaceNo, x, y, z, radius, divisions, density, int(is_opening)))

    def AddPolygonalRegionToSurface(self, surfaceNo: int, regionData):
        self._geometry.AddPolygonalRegionToSurface(surfaceNo, regionData)

    def GetParametricSurfaceCount(self):
        return self._geometry.GetParametricSurfaceCount()

    def GetParametricSurfaceInfo(self, surfaceNo: int):
        name = self._b.out_str()
        type_ = self._b.out_str()
        boundary_points_count = self._b.out_int()
        density_points_count = self._b.out_int()
        opening_count = self._b.out_int()
        region_count = self._b.out_int()
        self._geometry.GetParametricSurfaceInfo(
            surfaceNo, name.ref, type_.ref, boundary_points_count.ref,
            density_points_count.ref, opening_count.ref, region_count.ref
        )
        return (name.value, type_.value, boundary_points_count.value,
                density_points_count.value, opening_count.value, region_count.value)

    def GetParametricSurfaceInfoEx(self, surfaceNo: int):
        name = self._b.out_str()
        type_ = self._b.out_int()
        sub_type = self._b.out_str()
        num_vertices = self._b.out_int()
        mesh_size = self._b.out_double()
        num_divisions = self._b.out_int()
        meshing_method = self._b.out_int()
        is_quad = self._b.out_int()
        origin_node = self._b.out_int()
        x_node = self._b.out_int()
        y_node = self._b.out_int()
        num_circular_openings = self._b.out_int()
        num_polygonal_openings = self._b.out_int()
        num_circular_regions = self._b.out_int()
        num_polygonal_regions = self._b.out_int()
        num_density_points = self._b.out_int()
        num_density_lines = self._b.out_int()
        self._geometry.GetParametricSurfaceInfoEx(
            surfaceNo, name.ref, type_.ref, sub_type.ref, num_vertices.ref, mesh_size.ref,
            num_divisions.ref, meshing_method.ref, is_quad.ref, origin_node.ref, x_node.ref,
            y_node.ref, num_circular_openings.ref, num_polygonal_openings.ref,
            num_circular_regions.ref, num_polygonal_regions.ref, num_density_points.ref,
            num_density_lines.ref
        )
        return (name.value, type_.value, sub_type.value, num_vertices.value, mesh_size.value,
                num_divisions.value, meshing_method.value, bool(is_quad.value), origin_node.value,
                x_node.value, y_node.value, num_circular_openings.value, num_polygonal_openings.value,
                num_circular_regions.value, num_polygonal_regions.value, num_density_points.value,
                num_density_lines.value)

    def GetParametricSurfaceMeshInfo(self, surfaceNo: int):
        node_count = self._b.out_int()
        element_count = self._b.out_int()
        self._geometry.GetParametricSurfaceMeshInfo(surfaceNo, node_count.ref, element_count.ref)
        return (node_count.value, element_count.value)

    def GetParametricSurfaceMeshData(self, surfaceNo: int):
        node_count, element_count = self.GetParametricSurfaceMeshInfo(surfaceNo)
        nodes = self._b.out_int_array(node_count)
        elements = self._b.out_int_array(element_count)
        self._geometry.GetParametricSurfaceMeshData(surfaceNo, nodes.ref, elements.ref)
        return (nodes.value, elements.value)

    def SetParametricSurfaceUniqueID(self, surface_name: str, unique_id: str):
        self._geometry.SetParametricSurfaceUniqueID(surface_name, unique_id)

    def GetParametricSurfaceUniqueID(self, surface_name: str):
        return self._geometry.GetParametricSurfaceUniqueID(surface_name)

    def SetParametricSurfaceSubType(self, surfaceName: str, subType: str):
        self._geometry.SetParametricSurfaceSubType(surfaceName, subType)

    def GetParametricSurfaceSubType(self, surfaceName: str):
        return self._geometry.GetParametricSurfaceSubType(surfaceName)

    # ------------------------------------------------------------------ #
    # Intersección / merge
    # ------------------------------------------------------------------ #
    def IntersectBeams(self, method: int, beamList: list, tolerance: float):
        size = self.GetIntersectBeamsCount(beamList, tolerance)
        if size == 0 or method not in (1, 2):
            return []
        newIds = self._b.out_int_array(size)
        self._geometry.IntersectBeams(method, self._b.in_int_array(beamList), tolerance, newIds.ref)
        return newIds.value

    def MergeBeams(self, beamList: list, newId: int, property_id: int, beta_angle: float, material_name: str):
        return bool(self._geometry.MergeBeams(self._b.in_int_array(beamList), newId, property_id, beta_angle, material_name))

    def MergeNodes(self, new_Id: int, nodeList: list):
        return bool(self._geometry.MergeNodes(new_Id, self._b.in_int_array(nodeList)))

    def GetCountOfBreakableBeamsAtSpecificNodes(self, nodeList: list):
        return self._geometry.GetCountOfBreakableBeamsAtSpecificNodes(self._b.in_int_array(nodeList))

    def BreakBeamsAtSpecificNodes(self, nodeList: list):
        vt_nodeList = self._b.in_int_array(nodeList)
        size = self.GetCountOfBreakableBeamsAtSpecificNodes(nodeList)
        if size == 0:
            return ([], [])
        brokenIds = self._b.out_int_array(size)
        newIds = self._b.out_int_array(size)
        self._geometry.BreakBeamsAtSpecificNodes(vt_nodeList, brokenIds.ref, newIds.ref)
        return (brokenIds.value, newIds.value)

    def GetIntersectBeamsCount(self, beamList: list, tolerance: float):
        return self._geometry.GetIntersectBeamsCount(self._b.in_int_array(beamList), tolerance)

    # ------------------------------------------------------------------ #
    # Miembros físicos
    # ------------------------------------------------------------------ #
    def ClearPhysicalMemberSelection(self):
        self._geometry.ClearPhysicalMemberSelection()

    def CreatePhysicalMember(self, memberList: list):
        size = len(memberList)
        if size == 0:
            return
        return int(self._geometry.CreatePhysicalMember(size, self._b.in_int_array(memberList)))

    def DeletePhysicalMember(self, physicalMemberId: int):
        return bool(self._geometry.DeletePhysicalMember(physicalMemberId))

    def GetAnalyticalMemberCountForPhysicalMember(self, physicalMemberId: int):
        return int(self._geometry.GetAnalyticalMemberCountForPhysicalMember(physicalMemberId))

    def GetAnalyticalMembersForPhysicalMember(self, physicalMemberId: int):
        count = self.GetAnalyticalMemberCountForPhysicalMember(physicalMemberId)
        if count == 0:
            return []
        members = self._b.out_int_array(count)
        self._geometry.GetAnalyticalMembersForPhysicalMember(physicalMemberId, count, members.ref)
        return members.value

    def GetLastPhysicalMemberNo(self):
        return int(self._geometry.GetLastPhysicalMemberNo())

    def GetNoOfSelectedPhysicalMembers(self):
        return int(self._geometry.GetNoOfSelectedPhysicalMembers())

    def GetSelectedPhysicalMembers(self):
        count = self.GetNoOfSelectedPhysicalMembers()
        if count == 0:
            return []
        members = self._b.out_int_array(count)
        self._geometry.GetSelectedPhysicalMembers(members.ref)
        return members.value

    def GetPhysicalMemberCount(self):
        return int(self._geometry.GetPhysicalMemberCount())

    def GetPhysicalMemberList(self):
        count = self.GetPhysicalMemberCount()
        if count == 0:
            return []
        members = self._b.out_int_array(count)
        self._geometry.GetPhysicalMemberList(members.ref)
        return members.value

    def GetPhysicalMemberUniqueID(self, physicalMemberId: int):
        return self._geometry.GetPhysicalMemberUniqueID(physicalMemberId)

    def GetPMemberCount(self):
        return int(self._geometry.GetPMemberCount())

    def SelectMultiplePhysicalMembers(self, physicalMemberList: list):
        self._geometry.SelectMultiplePhysicalMembers(self._b.in_int_array(physicalMemberList))

    def SelectPhysicalMember(self, physicalMemberId: int):
        self._geometry.SelectPhysicalMember(physicalMemberId)

    def SetPhysicalMemberUniqueID(self, physicalMemberId: int, uniqueId: str):
        self._geometry.SetPhysicalMemberUniqueID(physicalMemberId, uniqueId)

    # ------------------------------------------------------------------ #
    # CIS2
    # ------------------------------------------------------------------ #
    def GetMemberIncidence_CIS2(self, memberId: int):
        uid = self._b.out_str()
        start_node = self._b.out_int()
        end_node = self._b.out_int()
        self._geometry.GetMemberIncidence_CIS2(memberId, uid.ref, start_node.ref, end_node.ref)
        return (uid.value, start_node.value, end_node.value)

    def GetNodeIncidence_CIS2(self, nodeId: int):
        uid = self._b.out_str()
        x = self._b.out_double()
        y = self._b.out_double()
        z = self._b.out_double()
        self._geometry.GetNodeIncidence_CIS2(nodeId, uid.ref, x.ref, y.ref, z.ref)
        return (uid.value, x.value, y.value, z.value)

    def GetPlateIncidence_CIS2(self, plateId: int):
        uid = self._b.out_str()
        outs = [self._b.out_int() for _ in range(4)]
        self._geometry.GetPlateIncidence_CIS2(plateId, uid.ref, *[o.ref for o in outs])
        return (uid.value, *[o.value for o in outs])

    def GetSolidIncidence_CIS2(self, solidId: int):
        uid = self._b.out_str()
        outs = [self._b.out_int() for _ in range(8)]
        self._geometry.GetSolidIncidence_CIS2(solidId, uid.ref, *[o.ref for o in outs])
        return (uid.value, *[o.value for o in outs])
