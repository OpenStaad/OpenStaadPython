from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Design():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._design = self._staad.Design

        self._functions= [
           'CreateDesignBrief',
           'AssignDesignCommand'
        ]

        for function_name in self._functions:
            self._design._FlagAsMethod(function_name)

    def CreateDesignBrief(self,design_code:int):
        """ 
        """
        self._design.CreateDesignBrief(design_code)

    def AssignDesignCommand(self,brief_reference:int,command_name:str,command_value:str,members:list[int]):
        """ 
        """
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)
        
        # Crear SAFEARRAY para 'release'
        safe_list_members = make_safe_array_long(members)
        members = make_variant_vt_ref(safe_list_members, automation.VT_ARRAY | automation.VT_I4)

        self._design.AssignDesignCommand(brief_reference,command_name,command_value,members)