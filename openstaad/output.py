from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Output():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._output = self._staad.Output

        self._functions= [
            'GetMemberEndForces',
            'GetModalMassParticipationFactors',
            'GetModeFrequency',
            'GetSupportReactions'
        ]

        for function_name in self._functions:
            self._output._FlagAsMethod(function_name)

    def GetMemberEndForces(self,beam, start = True, lc :int= 1,local: int = 0):
        """
        Get the end forces (FX, FY, FZ, MX, MY, MZ) at a specified end of a member for a given load case.
        """
        safe_n1 = make_safe_array_double(6)
        x = make_variant_vt_ref(safe_n1,  automation.VT_ARRAY |  automation.VT_R8)

        if start:
            end = 0
        else:
            end = 1

        retval = self._output.GetMemberEndForces(beam, end,lc,x,local)

        return x.value[0]

    def GetModalMassParticipationFactors(self, var_mode: int):
        """
        Get the modal mass participation factors in X, Y and Z directions for a given mode.
        """
        patX = ctypes.c_double() 
        patY = ctypes.c_double()
        patZ = ctypes.c_double()
        
        retval = self._output.GetModalMassParticipationFactors(var_mode, ctypes.byref(patX), ctypes.byref(patY), ctypes.byref(patZ))
        
        return (round(patX.value,5), round(patY.value,5), round(patZ.value,5))
    
    def GetModeFrequency(self, var_mode:int):
        """
        Get the natural frequency (Hz) for a given mode.
        """
        frequency = ctypes.c_double() 
        
        retval = self._output.GetModeFrequency(var_mode, ctypes.byref(frequency))
        
        return (round(frequency.value,3))
    
    def GetSupportReactions(self, node: int,lc :int= 1):
        """
        Get the support reactions (FX, FY, FZ, MX, MY, MZ) at a specified node for a given load case.
        """
        safe_n1 = make_safe_array_double(6)
        x = make_variant_vt_ref(safe_n1,  automation.VT_ARRAY |  automation.VT_R8)

        retval = self._output.GetSupportReactions(node,lc,x)

        return x.value[0]
    
    
    