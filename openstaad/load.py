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
            self._load._FlagAsMethod(function_name)

    def GetLoadCaseTitle(self,lc):
        return self._load.GetLoadCaseTitle(lc)
