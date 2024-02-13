from openstaad.tools import *
from comtypes import automation
from comtypes import client

from .geometry import Geometry

class View():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._view = self._staad.View
        self._geometry = Geometry()

        self._functions= [
            "RefreshView",
            "ShowAllMembers",
            "HideAllMembers",
            "ZoomExtentsMainView",
            "ShowMembers",
            "HideMember",
            "HideMembers",
            "ShowBack",
            "ShowBottom",
            "ShowFront",
            "ShowIsometric",
            "ShowLeft",
            "ShowPlan",
            "ShowRight",
            "SpinLeft",
            "SpinRight",
            "ZoomAll"
        ]

        for function_name in self._functions:
            self._view._FlagAsMethod(function_name)

    def RefreshView(self):
        self._view.RefreshView()

    def ShowAllMembers(self):
        self._view.ShowAllMembers()
    
    def HideAllMembers(self):
        self._view.HideAllMembers()

    def ZoomExtentsMainView(self):
        self._view.ZoomExtentsMainView()

    def ShowMembers(self,NMembers,NaMemberNos):
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._view.ShowAllMembers()
        self._view.HideAllMembers()
        self._geometry.ClearMemberSelection() 
        self._view.ShowMembers(NMembers,lista_variant)
        self._view.ShowIsometric()
        self._view.ZoomExtentsMainView()
        self._view.RefreshView()

    def HideMember(self,IDMember):
        self._view.HideMember(IDMember)
        self._view.RefreshView()

    def HideMembers(self,NMembers,NaMemberNos):
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._view.HideMembers(NMembers,lista_variant)
        self._view.RefreshView()

    def ShowBack(self):
        self._view.ShowBack()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowBottom(self):
        self._view.ShowBottom()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowFront(self):
        self._view.ShowFront()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowIsometric(self):
        self._view.ShowIsometric()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()
        
    def ShowLeft(self):
        self._view.ShowLeft()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowPlan(self):
        self._view.ShowPlan()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowRight(self):
        self._view.ShowRight()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def SpinLeft(self,Degrees):
        Degrees = float(Degrees)
        self._view.SpinLeft(Degrees)
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()
                
    def SpinRight(self,Degrees):
        Degrees = float(Degrees)
        self._view.SpinRight(Degrees)
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ZoomAll(self):
        self._view.ZoomAll()
    
