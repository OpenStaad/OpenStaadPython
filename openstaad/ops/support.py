"""
support.py — dominio Support del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code` (sin manejo de errores por ahora); se conservan
los condicionales que son *lógica de retorno* (p.ej. devolver [] si count==0).
"""

from .bridge import Bridge
from ._com import acquire
from ._coerce import as_id, as_id_list


class Support:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._support = staad.Support

        self._functions = [
            "AssignSupportToNode", "CreateSupportFixed", "CreateSupportPinned",
            "CreateSupportFixedBut", "GetSupportCount", "GetSupportNodes",
            "GetSupportType", "GetSupportInformation", "GetSupportUniqueID",
            "SetSupportUniqueID", "RemoveSupportFromNode", "DeleteSupport",
            "GetSupportName", "GetSupportInformationEx", "CreateInclinedSupport",
            "CreateElasticMat", "GetCountOfElasticMat", "GetElasticMatDetail",
            "GetElasticMatAssignmentList", "RemoveElasticMat", "RemoveElasticMatFromNode",
            "AssignSupportToEntityList", "CreatePlateMat", "GetCountOfPlateMat",
            "GetPlateMatSupportId", "GetPlateMatDetail", "GetPlateMatAssignmentList",
            "RemovePlateMat", "RemovePlateMatFromPlate", "CreateElasticFooting",
            "GetCountOfElasticFooting", "GetElasticFootingDetail",
            "GetElasticFootingAssignmentList", "RemoveElasticFooting",
            "RemoveElasticFootingFromNode",
        ]
        for function_name in self._functions:
            self._support._FlagAsMethod(function_name)

    # ---- supports básicos ----
    def AssignSupportToNode(self, NodeID, SupportID: int) -> bool:
        """Asigna un soporte a UN nodo. Devuelve True si STAAD la aceptó.

        El método COM procesa un solo nodo por llamada: pasarle un array asigna
        únicamente el primer elemento, sin error. Por eso aquí se rechaza
        cualquier colección — para varios nodos usa `AssignSupportToNodes`.
        """
        return self._assign_support_to_one(
            as_id(NodeID, "NodeID", "AssignSupportToNodes"), SupportID
        )

    def AssignSupportToNodes(self, NodeIDs, SupportID: int) -> bool:
        """Asigna un soporte a uno o varios nodos (int, lista, tupla, iterable).

        Devuelve True si **todas** las asignaciones fueron aceptadas.

        No forma parte de la API oficial de OpenSTAAD: existe porque el método
        COM es de un nodo por llamada. Ver `AssignSupportToNode`.
        """
        results = [
            self._assign_support_to_one(node_id, SupportID)
            for node_id in as_id_list(NodeIDs, "NodeIDs")
        ]
        return all(results)

    def _assign_support_to_one(self, NodeID: int, SupportID: int) -> bool:
        """Única llamada COM de asignación: el punto que ambas variantes comparten.

        Aislado a propósito. Si algún día se confirma que
        `AssignSupportToEntityList` acepta nodos y es más rápido, se sustituye
        aquí el bucle por una sola llamada sin tocar la superficie pública.
        """
        retval = self._support.AssignSupportToNode(NodeID, SupportID)
        # El oficial trata retval < 0 como error; no todas las versiones COM
        # devuelven algo, y en ese caso no hay nada que interpretar.
        return retval is None or retval >= 0

    def CreateSupportFixed(self):
        return self._support.CreateSupportFixed()

    def CreateSupportPinned(self):
        return self._support.CreateSupportPinned()

    def CreateSupportFixedBut(self, ReleaseSpec: list, SpringSpec: list):
        release = self._b.in_double_array_variant(ReleaseSpec)
        spring = self._b.in_double_array_variant(SpringSpec)
        return self._support.CreateSupportFixedBut(release.ref, spring.ref)

    def GetSupportCount(self):
        return self._support.GetSupportCount()

    def GetSupportNodes(self):
        count = self.GetSupportCount()
        nodes = self._b.out_int_array(count)
        self._support.GetSupportNodes(nodes.ref)
        return nodes.value

    def GetSupportType(self, nodeNo: int):
        return self._support.GetSupportType(nodeNo)

    def GetSupportInformation(self, nodeNo: int):
        """(tipo, release[6], spring[6])."""
        release = self._b.out_int_array(6)
        spring = self._b.out_double_array(6)
        stype = self._support.GetSupportInformation(nodeNo, release.ref, spring.ref)
        return (stype, release.value, spring.value)

    def GetSupportUniqueID(self, supportNo: int):
        return self._support.GetSupportUniqueID(supportNo)

    def SetSupportUniqueID(self, supportNo: int, guid: str):
        self._support.SetSupportUniqueID(supportNo, guid)

    def RemoveSupportFromNode(self, NodeIDs: list):
        self._support.RemoveSupportFromNode(self._b.in_int_array_variant(NodeIDs).ref)

    def DeleteSupport(self, supportNo: int):
        return self._support.DeleteSupport(supportNo)

    def GetSupportName(self, supportNo: int):
        return self._support.GetSupportName(supportNo)

    def GetSupportInformationEx(self, nodeNo: int):
        """(supportNo, supportType, release[6], spring[6])."""
        supportNo = self._b.out_int()
        supportType = self._b.out_int()
        release = self._b.out_int_array(6)
        spring = self._b.out_double_array(6)
        self._support.GetSupportInformationEx(
            nodeNo, supportNo.ref, supportType.ref, release.ref, spring.ref
        )
        return (supportNo.value, supportType.value, release.value, spring.value)

    def CreateInclinedSupport(self, inclinedType: int, refType: int, refNode: int, coord, releaseSpec: list, springSpec: list):
        return self._support.CreateInclinedSupport(
            inclinedType, refType, refNode,
            self._b.in_double_array(coord),
            self._b.in_double_array(releaseSpec),
            self._b.in_double_array(springSpec),
        )

    # ---- elastic mat ----
    def CreateElasticMat(self, direction, subgrade, printFlag, springType):
        return self._support.CreateElasticMat(direction, subgrade, printFlag, springType)

    def GetCountOfElasticMat(self):
        return self._support.GetCountOfElasticMat()

    def GetElasticMatDetail(self, supportid):
        """(direction, subgrade, printFlag, springType, nodesCount)."""
        direction = self._b.out_int()
        subgrade = self._b.out_double()
        printFlag = self._b.out_int()
        springType = self._b.out_int()
        nodesCount = self._b.out_int()
        self._support.GetElasticMatDetail(
            supportid, direction.ref, subgrade.ref, printFlag.ref, springType.ref, nodesCount.ref
        )
        return (direction.value, subgrade.value, bool(printFlag.value), springType.value, nodesCount.value)

    def GetElasticMatAssignmentList(self, supportid):
        _, _, _, _, nodesCount = self.GetElasticMatDetail(supportid)
        if nodesCount == 0:
            return []
        nodes = self._b.out_int_array(nodesCount)
        retval = self._support.GetElasticMatAssignmentList(supportid, nodes.ref)
        if not bool(retval):
            return []
        return nodes.value

    def RemoveElasticMat(self, supportid):
        return self._support.RemoveElasticMat(supportid)

    def RemoveElasticMatFromNode(self, nodeid):
        return bool(self._support.RemoveElasticMatFromNode(nodeid))

    def AssignSupportToEntityList(self, supportid, entitylist):
        return bool(self._support.AssignSupportToEntityList(supportid, self._b.in_int_array(entitylist)))

    # ---- plate mat ----
    def CreatePlateMat(self, direction: int, subgrades, printFlag: bool, springType: int):
        if isinstance(subgrades, float):
            subgrades = [subgrades]
        return self._support.CreatePlateMat(direction, self._b.in_double_array(subgrades), int(printFlag), springType)

    def GetCountOfPlateMat(self):
        return self._support.GetCountOfPlateMat()

    def GetPlateMatSupportId(self, plateMatIndex):
        return self._support.GetPlateMatSupportId(plateMatIndex)

    def GetPlateMatDetail(self, plateMatNo):
        """(direction, subgrade1, subgrade2, subgrade3, printFlag, springType, nAssignedPlateCount)."""
        direction = self._b.out_int()
        subgrade1 = self._b.out_double()
        subgrade2 = self._b.out_double()
        subgrade3 = self._b.out_double()
        printFlag = self._b.out_int()
        springType = self._b.out_int()
        nAssignedPlateCount = self._b.out_int()
        self._support.GetPlateMatDetail(
            plateMatNo, direction.ref, subgrade1.ref, subgrade2.ref, subgrade3.ref,
            printFlag.ref, springType.ref, nAssignedPlateCount.ref
        )
        return (direction.value, subgrade1.value, subgrade2.value, subgrade3.value,
                printFlag.value, springType.value, nAssignedPlateCount.value)

    def GetPlateMatAssignmentList(self, plateMatNo):
        *_, nAssignedPlateCount = self.GetPlateMatDetail(plateMatNo)
        if nAssignedPlateCount == 0:
            return []
        plates = self._b.out_int_array(nAssignedPlateCount)
        retval = self._support.GetPlateMatAssignmentList(plateMatNo, plates.ref)
        if not bool(retval):
            return []
        return plates.value

    def RemovePlateMat(self, supportId):
        return bool(self._support.RemovePlateMat(supportId))

    def RemovePlateMatFromPlate(self, plateNo: int):
        return bool(self._support.RemovePlateMatFromPlate(plateNo))

    # ---- elastic footing ----
    def CreateElasticFooting(self, length, width, direction, subgrade):
        return self._support.CreateElasticFooting(length, width, direction, subgrade)

    def GetCountOfElasticFooting(self):
        return self._support.GetCountOfElasticFooting()

    def GetElasticFootingDetail(self, supportid):
        """(length, width, direction, subgrade, nodesCount)."""
        length = self._b.out_double()
        width = self._b.out_double()
        direction = self._b.out_int()
        subgrade = self._b.out_double()
        nodesCount = self._b.out_int()
        self._support.GetElasticFootingDetail(
            supportid, length.ref, width.ref, direction.ref, subgrade.ref, nodesCount.ref
        )
        return (length.value, width.value, direction.value, subgrade.value, nodesCount.value)

    def GetElasticFootingAssignmentList(self, supportid):
        _, _, _, _, nodesCount = self.GetElasticFootingDetail(supportid)
        if nodesCount == 0:
            return []
        nodes = self._b.out_int_array(nodesCount)
        retval = self._support.GetElasticFootingAssignmentList(supportid, nodes.ref)
        if retval == 0:
            return []
        return nodes.value

    def RemoveElasticFooting(self, supportid):
        return self._support.RemoveElasticFooting(supportid)

    def RemoveElasticFootingFromNode(self, nodeid):
        return self._support.RemoveElasticFootingFromNode(nodeid)
