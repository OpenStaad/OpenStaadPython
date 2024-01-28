from openstaad.Safe_variables import *
from comtypes import automation

class _Load():
    def __init__(self,os):
        self._os = os.Load

        self._functions= [
            'GetLoadCaseTitle'
        ]

        for function_name in self._functions:
            self._os._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def GetLoadCaseTitle(self,lc):
        return self._os.GetLoadCaseTitle(lc)
