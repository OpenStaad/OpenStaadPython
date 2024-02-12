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
            self._os._FlagAsMethod(function_name)

    def RefreshView(self):
        self._os.RefreshView()

    def ShowAllMembers(self):
        self._os.ShowAllMembers()
    
    def HideAllMembers(self):
        self._os.HideAllMembers()

    def ZoomExtentsMainView(self):
        self._os.ZoomExtentsMainView()

    def ShowMembers(self,NMembers,NaMemberNos):
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._os.ShowAllMembers()
        self._os.HideAllMembers()
        self._geometry.ClearMemberSelection() 
        self._os.ShowMembers(NMembers,lista_variant)
        self._os.ShowIsometric()
        self._os.ZoomExtentsMainView()
        self._os.RefreshView()

    def HideMember(self,IDMember):
        self._os.HideMember(IDMember)
        self._os.RefreshView()

    def HideMembers(self,NMembers,NaMemberNos):
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._os.HideMembers(NMembers,lista_variant)
        self._os.RefreshView()

    def ShowBack(self):
        self._os.ShowBack()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ShowBottom(self):
        self._os.ShowBottom()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ShowFront(self):
        self._os.ShowFront()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ShowIsometric(self):
        self._os.ShowIsometric()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()
        
    def ShowLeft(self):
        self._os.ShowLeft()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ShowPlan(self):
        self._os.ShowPlan()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ShowRight(self):
        self._os.ShowRight()
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def SpinLeft(self,Degrees):
        Degrees = float(Degrees)
        self._os.SpinLeft(Degrees)
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()
                
    def SpinRight(self,Degrees):
        Degrees = float(Degrees)
        self._os.SpinRight(Degrees)
        self._os.RefreshView()
        self._os.ZoomExtentsMainView()

    def ZoomAll(self):
        self._os.ZoomAll()
    
