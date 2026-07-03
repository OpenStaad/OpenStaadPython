"""
view.py — dominio View del subpaquete ops, sobre bridge.

Métodos alineados al comportamiento del oficial (PascalCase). Se omiten los
`raise_os_error_if_error_code`. Muchos métodos hacen RefreshView/ZoomExtents tras
la acción, igual que el oficial.
"""

from .bridge import Bridge
from ._com import acquire


class View:
    def __init__(self, connection=None, bridge=None, filePath=None):
        staad = connection if connection is not None else acquire(filePath)
        self._b = bridge if bridge is not None else Bridge()
        self._view = staad.View

        # ShowMembers necesita ClearMemberSelection (de Geometry); se llama directo
        # al sub-objeto COM para no acoplar con la clase Geometry.
        self._geometry_com = staad.Geometry
        self._geometry_com._FlagAsMethod("ClearMemberSelection")

        self._functions = [
            "RefreshView", "ShowAllMembers", "HideAllMembers", "ZoomExtentsMainView",
            "ShowMembers", "HideMember", "HideMembers", "ShowBack", "ShowBottom",
            "ShowFront", "ShowIsometric", "ShowLeft", "ShowPlan", "ShowRight",
            "SpinLeft", "SpinRight", "ZoomAll", "GetApplicationDesktopSize",
            "SetWindowPosition", "RotateUp", "RotateDown", "RotateLeft", "RotateRight",
            "CreateNewViewForSelections", "SetLabel", "SetSectionView", "SetDiagramMode",
            "SetNodeAnnotationMode", "SetReactionAnnotationMode", "GetInterfaceMode",
            "SetInterfaceMode", "SetModeSectionPage", "SetBeamAnnotationMode", "ShowMember",
            "SetUnits", "HidePlate", "HideSolid", "HideSurface", "HideEntity",
            "SelectMembersParallelTo", "SelectGroup", "SelectInverse", "SelectByItemList",
            "SelectByMissingAttribute", "SelectEntitiesConnectedToNode",
            "SelectEntitiesConnectedToMember", "SelectEntitiesConnectedToPlate",
            "SelectEntitiesConnectedToSolid", "GetNoOfBeamsInView", "GetBeamsInView",
            "CreateNewViewForSelectionsEx", "ExportView", "CopyPicture", "GetScaleValues",
            "SetScaleValues", "GetScaleValueByType", "SetScaleValueByType", "GetScaleCount",
            "DetachView", "RenameView", "OpenView", "SaveView", "GetWindowTitle",
            "GetWindowCount", "CloseActiveWindow", "SetActiveWindow", "SetDesignResults",
        ]
        for function_name in self._functions:
            self._view._FlagAsMethod(function_name)

    def _refresh_zoom(self):
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    # ---- vistas / navegación ----
    def RefreshView(self):
        self._view.RefreshView()

    def ShowAllMembers(self):
        self._view.ShowAllMembers()

    def HideAllMembers(self):
        self._view.HideAllMembers()

    def ZoomExtentsMainView(self):
        self._view.ZoomExtentsMainView()

    def ShowMembers(self, NMembers, NaMemberNos):
        members = self._b.in_int_array_variant(NaMemberNos)
        self._view.ShowAllMembers()
        self._view.HideAllMembers()
        self._geometry_com.ClearMemberSelection()
        self._view.ShowMembers(NMembers, members.ref)
        self._view.ShowIsometric()
        self._view.ZoomExtentsMainView()
        self._view.RefreshView()

    def HideMember(self, IDMember):
        self._view.HideMember(IDMember)
        self._view.RefreshView()

    def HideMembers(self, NMembers, NaMemberNos):
        members = self._b.in_int_array_variant(NaMemberNos)
        self._view.HideMembers(NMembers, members.ref)
        self._view.RefreshView()

    def ShowBack(self):
        self._view.ShowBack()
        self._refresh_zoom()

    def ShowBottom(self):
        self._view.ShowBottom()
        self._refresh_zoom()

    def ShowFront(self):
        self._view.ShowFront()
        self._refresh_zoom()

    def ShowIsometric(self):
        self._view.ShowIsometric()
        self._refresh_zoom()

    def ShowLeft(self):
        self._view.ShowLeft()
        self._refresh_zoom()

    def ShowPlan(self):
        self._view.ShowPlan()
        self._refresh_zoom()

    def ShowRight(self):
        self._view.ShowRight()
        self._refresh_zoom()

    def SpinLeft(self, Degrees):
        self._view.SpinLeft(float(Degrees))
        self._refresh_zoom()

    def SpinRight(self, Degrees):
        self._view.SpinRight(float(Degrees))
        self._refresh_zoom()

    def ZoomAll(self):
        self._view.ZoomAll()

    def GetApplicationDesktopSize(self):
        """(L, W) del escritorio de la aplicación."""
        L = self._b.out_int()
        W = self._b.out_int()
        self._view.GetApplicationDesktopSize(L.ref, W.ref)
        return (L.value, W.value)

    def SetWindowPosition(self, xTop, yTop, xWindow, yWindow):
        self._view.SetWindowPosition(xTop, yTop, xWindow, yWindow)

    def RotateUp(self, dDegrees: float):
        self._view.RotateUp(dDegrees)
        self._refresh_zoom()

    def RotateDown(self, dDegrees: float):
        self._view.RotateDown(dDegrees)
        self._refresh_zoom()

    def RotateLeft(self, dDegrees: float):
        self._view.RotateLeft(dDegrees)
        self._refresh_zoom()

    def RotateRight(self, dDegrees: float):
        self._view.RotateRight(dDegrees)
        self._refresh_zoom()

    def CreateNewViewForSelections(self):
        return self._view.CreateNewViewForSelections()

    def SetLabel(self, which: int, showFlag: bool):
        return self._view.SetLabel(which, showFlag)

    def SetSectionView(self, plane: int, minVal: float, maxVal: float):
        self._view.SetSectionView(plane, minVal, maxVal)
        self._refresh_zoom()

    def SetDiagramMode(self, which: int, showFlag: bool, refreshFlag: bool):
        self._view.SetDiagramMode(which, showFlag, refreshFlag)
        self._refresh_zoom()

    def SetNodeAnnotationMode(self, dFlag: bool, refreshFlag: bool):
        self._view.SetNodeAnnotationMode(dFlag, refreshFlag)
        self._refresh_zoom()

    def SetReactionAnnotationMode(self, dFlag: bool, refreshFlag: bool):
        self._view.SetReactionAnnotationMode(dFlag, refreshFlag)
        self._refresh_zoom()

    def GetInterfaceMode(self):
        return self._view.GetInterfaceMode()

    def SetInterfaceMode(self, interfaceMode: int):
        self._view.SetInterfaceMode(interfaceMode)
        self._refresh_zoom()

    def SetModeSectionPage(self, interfaceMode: int, sectionNumber: int, pageNumber: int):
        self._view.SetModeSectionPage(interfaceMode, sectionNumber, pageNumber)
        self._refresh_zoom()

    def SetBeamAnnotationMode(self, Type: int, DWFlags: int, RefreshFlag: bool):
        self._view.SetBeamAnnotationMode(Type, DWFlags, RefreshFlag)
        self._refresh_zoom()

    def ShowMember(self, nMember: int):
        self._view.ShowMember(nMember)
        self._refresh_zoom()

    def SetUnits(self, uType: int, strUnit: str):
        self._view.SetUnits(uType, strUnit)
        self._refresh_zoom()

    def HidePlate(self, nPlate: int):
        self._view.HidePlate(nPlate)
        self._refresh_zoom()

    def HideSolid(self, nSolid: int):
        self._view.HideSolid(nSolid)
        self._refresh_zoom()

    def HideSurface(self, nSurface: int):
        self._view.HideSurface(nSurface)
        self._refresh_zoom()

    def HideEntity(self, nEntity: int):
        self._view.HideEntity(nEntity)
        self._refresh_zoom()

    # ---- selección ----
    def SelectMembersParallelTo(self, bstrAxis: str):
        self._view.SelectMembersParallelTo(bstrAxis)
        self._refresh_zoom()

    def SelectGroup(self, bstrGroup: str):
        return self._view.SelectGroup(bstrGroup)

    def SelectInverse(self, entityType: int):
        self._view.SelectInverse(entityType)
        self._refresh_zoom()

    def SelectByItemList(self, entityType: int, nItems: int, itemList: list):
        self._view.SelectByItemList(entityType, nItems, self._b.in_int_array(itemList))
        self._refresh_zoom()

    def SelectByMissingAttribute(self, attributeCode: int):
        self._view.SelectByMissingAttribute(attributeCode)
        self._refresh_zoom()

    def SelectEntitiesConnectedToNode(self, entityType: int, nodeNo: int):
        self._view.SelectEntitiesConnectedToNode(entityType, nodeNo)
        self._refresh_zoom()

    def SelectEntitiesConnectedToMember(self, entityType: int, memberNo: int):
        self._view.SelectEntitiesConnectedToMember(entityType, memberNo)
        self._refresh_zoom()

    def SelectEntitiesConnectedToPlate(self, entityType: int, plateNo: int):
        self._view.SelectEntitiesConnectedToPlate(entityType, plateNo)
        self._refresh_zoom()

    def SelectEntitiesConnectedToSolid(self, entityType: int, solidNo: int):
        self._view.SelectEntitiesConnectedToSolid(entityType, solidNo)
        self._refresh_zoom()

    def GetNoOfBeamsInView(self):
        return self._view.GetNoOfBeamsInView()

    def GetBeamsInView(self, nBeamList: list):
        return self._view.GetBeamsInView(self._b.in_int_array(nBeamList))

    # ---- ventanas / export / escalas ----
    def CreateNewViewForSelectionsEx(self, windowOptions: int):
        return self._view.CreateNewViewForSelectionsEx(windowOptions)

    def ExportView(self, FileLocation: str, FileName: str, FileFormat: int, Overwrite: bool):
        return self._view.ExportView(FileLocation, FileName, FileFormat, Overwrite)

    def CopyPicture(self):
        """(xDim, yDim) de la imagen copiada."""
        xDim = self._b.out_int()
        yDim = self._b.out_int()
        self._view.CopyPicture(xDim.ref, yDim.ref)
        return (xDim.value, yDim.value)

    def GetScaleValues(self):
        count = self._view.GetScaleCount()
        scales = self._b.out_double_array(count)
        self._view.GetScaleValues(scales.ref)
        return scales.value

    def SetScaleValues(self, ScalesList: list):
        return self._view.SetScaleValues(self._b.in_double_array(ScalesList))

    def GetScaleValueByType(self, scaleTypeId: int):
        value = self._b.out_double()
        self._view.GetScaleValueByType(scaleTypeId, value.ref)
        return value.value

    def SetScaleValueByType(self, scaleTypeId: int, value: float):
        return self._view.SetScaleValueByType(scaleTypeId, value)

    def GetScaleCount(self):
        return self._view.GetScaleCount()

    def DetachView(self):
        return self._view.DetachView()

    def RenameView(self, viewName: str):
        return self._view.RenameView(viewName)

    def OpenView(self, viewName: str, windowOptions: bool):
        return self._view.OpenView(viewName, windowOptions)

    def SaveView(self, viewName: str, overWrite: bool):
        return self._view.SaveView(viewName, overWrite)

    def GetWindowTitle(self, id: int):
        return self._view.GetWindowTitle(id)

    def GetWindowCount(self):
        return self._view.GetWindowCount()

    def CloseActiveWindow(self):
        return self._view.CloseActiveWindow()

    def SetActiveWindow(self, id: int):
        return self._view.SetActiveWindow(id)

    def SetDesignResults(self, utilization: int, color: bool, showValues: bool):
        return self._view.SetDesignResults(utilization, color, showValues)
