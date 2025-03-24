from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Load():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._load = self._staad.Load

        self._functions= [
            'GetLoadCaseTitle',
            'AddMemberConcForce',
            'SetLoadActive',
            'CreateNewPrimaryLoad'
        ]

        for function_name in self._functions:
            self._load._FlagAsMethod(function_name)

    def GetLoadCaseTitle(self,lc):
        return self._load.GetLoadCaseTitle(lc)
    
    def AddMemberConcForce(self,varBeamNo:list[int],varDirection:int,varForce:float,varD1:float,varD2:float):

        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        safe_list = make_safe_array_long(varBeamNo)
        varBeamNo = make_variant_vt_ref(safe_list, automation.VT_ARRAY | automation.VT_I4)

        self._load.AddMemberConcForce(varBeamNo,varDirection,varForce,varD1,varD2)
        
    def SetLoadActive(self,varLoadNo:int):
        self._load.SetLoadActive(varLoadNo)

    def CreateNewPrimaryLoad(self,LoadTitle:str="LOAD CASE X"):
        self._load.CreateNewPrimaryLoad(LoadTitle)