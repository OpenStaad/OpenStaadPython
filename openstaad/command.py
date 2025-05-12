from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Command():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._command = self._staad.Command

        self._functions= [
           'PerformAnalysis',
           'CreateSteelDesignCommand'
        ]

        for function_name in self._functions:
            self._command._FlagAsMethod(function_name)

    def PerformAnalysis(self,print_option:int):
        """ 
        --> 1 - Print Load Data
        --> 2 - Print Statics Check
        --> 3 - Print Static Load
        --> 4 - Print Mode Shapes
        --> 5 - Print Both
        --> 6 - Print All
        --> 0 - No Print
        """
        self._command.PerformAnalysis(print_option)

    def CreateSteelDesignCommand(self,design_code:int, command_no:int,int_values:list[int],float_values:float,string_values:str,member_list:list[int]):
        
        def make_safe_array_long(array):
            size = len(array)
            return automation._midlSAFEARRAY(ctypes.c_long).create(array)

        safe_list_members = make_safe_array_long(member_list)
        member_list = make_variant_vt_ref(safe_list_members, automation.VT_ARRAY | automation.VT_I4)

        safe_list_int = make_safe_array_long(int_values)
        int_values = make_variant_vt_ref(safe_list_int, automation.VT_ARRAY | automation.VT_I4)

        self._command.CreateSteelDesignCommand(design_code,command_no,int_values,float_values,string_values,member_list)



