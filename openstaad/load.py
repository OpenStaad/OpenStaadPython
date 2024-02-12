from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Load():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._load = self._staad.Load

        self._functions= [
            'GetLoadCaseTitle'
        ]

        for function_name in self._functions:
            self._os._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def GetLoadCaseTitle(self,lc):
        return self._os.GetLoadCaseTitle(lc)
