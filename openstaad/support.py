from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Support():

    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._support = self._staad.Support

        self._functions= [
            'CreateSupportFixed',
            'CreateSupportPinned',
            'AssignSupportToNode',
            'GetSupportCount',
            'GetSupportNodes'
        ]

        for function_name in self._functions:
            self._support._FlagAsMethod(function_name)

    ## SUPPORT FUNCTIONS

    def CreateSupportFixed(self):
        self._support.CreateSupportFixed()

    def CreateSupportPinned(self):
        self._support.CreateSupportPinned()

    def AssignSupportToNode(self,NoNode:int,Support_type_ID:int):
        self._support.AssignSupportToNode(NoNode,Support_type_ID)
    
    def GetSupportCount(self):
        return (self._support.GetSupportCount())

    def GetSupportNodes(self):
        n_supports = self._support.GetSupportCount()

        safe_list = make_safe_array_long(n_supports)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._support.GetSupportNodes(lista)

        return (lista[0])