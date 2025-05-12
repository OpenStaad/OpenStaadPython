from openstaad.tools import *
from comtypes import automation
from comtypes import client

from .geometry import Geometry

class View():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._view = self._staad.View
        self._geometry = Geometry()

        self._functions = [
            "GetBeamsInView",
            "GetNoOfBeamsInView",
            "HideAllMembers",
            "HideMember",
            "HideMembers",
            "RefreshView",
            "SelectMembersParallelTo",
            "ShowAllMembers",
            "ShowBack",
            "ShowBottom",
            "ShowFront",
            "ShowIsometric",
            "ShowLeft",
            "ShowMembers",
            "ShowPlan",
            "ShowRight",
            "SpinLeft",
            "SpinRight",
            "ZoomAll",
            "ZoomExtentsMainView"
        ]

        for function_name in self._functions:
            self._view._FlagAsMethod(function_name)

    def GetBeamsInView(self):
        """
        Get a list of beam IDs currently visible in the view.
        """
        beams=self._view.GetNoOfBeamsInView()
        safe_list = make_safe_array_long(beams)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._view.GetBeamsInView(lista)
        
        return (lista[0])
    
    def GetNoOfBeamsInView(self):
        """
        Get the number of beams currently visible in the view.
        """
        return self._view.GetNoOfBeamsInView()
    
    def HideAllMembers(self):
        """
        Hide all members from the view.
        """
        self._view.HideAllMembers()
    
    def HideMember(self,IDMember:int):
        """
        Hide a single member from the view.
        """
        self._view.HideMember(IDMember)
        self._view.RefreshView()

    def HideMembers(self,NaMemberNos:list):
        """
        Hide multiple members from the view.
        """
        Nmembers=len(NaMemberNos)
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)
        
        self._view.HideMembers(Nmembers,lista_variant)
        self._view.RefreshView()
    
    def RefreshView(self):
        """
        Refresh the viewing window.
        """
        self._view.RefreshView()

    def SelectMembersParallelTo(self,axis:str="X"):
        """
        Select members parallel to the specified axis.
        """
        self._view.SelectMembersParallelTo(axis)

    def ShowAllMembers(self):
        """
        Show all members.
        """
        self._view.ShowAllMembers()
    
    def ShowBack(self):
        """
        Show the back view of the model.
        """
        self._view.ShowBack()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowBottom(self):
        """
        Show the bottom view of the model.
        """
        self._view.ShowBottom()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowFront(self):
        """
        Show the front view of the model.
        """
        self._view.ShowFront()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowIsometric(self):
        """
        Show an isometric view of the model.
        """
        self._view.ShowIsometric()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()
        
    def ShowLeft(self):
        """
        Show the left view of the model.
        """
        self._view.ShowLeft()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowMembers(self,NaMemberNos:list):
        """
        Show only the specified members in the model view.
        """
        Nmembers=len(NaMemberNos)
        safe_list = make_safe_array_long_input(NaMemberNos)
        lista_variant = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._view.ShowAllMembers()
        self._view.HideAllMembers()
        self._geometry.ClearMemberSelection() 
        self._view.ShowMembers(Nmembers,lista_variant)
        self._view.ShowIsometric()
        self._view.ZoomExtentsMainView()
        self._view.RefreshView()
    
    def ShowPlan(self):
        """
        Show the top plan view of the model.
        """
        self._view.ShowPlan()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ShowRight(self):
        """
        Show the right view of the model.
        """
        self._view.ShowRight()
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def SpinLeft(self,Degrees:float):
        """
        Spin the model view to the left by a specified degree.
        """
        Degrees = float(Degrees)
        self._view.SpinLeft(Degrees)
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()
                
    def SpinRight(self,Degrees:float):
        """
        Spin the model view to the right by a specified degree.
        """
        Degrees = float(Degrees)
        self._view.SpinRight(Degrees)
        self._view.RefreshView()
        self._view.ZoomExtentsMainView()

    def ZoomAll(self):
        """
        Zoom all objects in the view.
        """
        self._view.ZoomAll()

    def ZoomExtentsMainView(self):
        """
        Display the whole structure.
        """
        self._view.ZoomExtentsMainView()

    

    
    
