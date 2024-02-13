from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Output():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._output = self._staad.Output

        self._functions= [
            'GetMemberEndForces',
            'GetSupportReactions'
        ]

        for function_name in self._functions:
            self._output._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def GetMemberEndForces(self,beam, start = True, lc :int= 1,local: int = 0):
        safe_n1 = make_safe_array_double(6)
        x = make_variant_vt_ref(safe_n1,  automation.VT_ARRAY |  automation.VT_R8)

        if start:
            end = 0
        else:
            end = 1

        retval = self._output.GetMemberEndForces(beam, end,lc,x,local)

        return x.value[0]

    def GetSupportReactions(self, node,lc :int= 1):
        safe_n1 = make_safe_array_double(6)
        x = make_variant_vt_ref(safe_n1,  automation.VT_ARRAY |  automation.VT_R8)

        retval = self._output.GetSupportReactions(node,lc,x)

        return x.value[0]