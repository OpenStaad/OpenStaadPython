from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Support():

    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._support = self._staad.Support

        self._functions= [
            'AssignSupportToNode',
            'CreateSupportFixed',
            'CreateSupportPinned',
            'GetSupportCount',
            'GetSupportNodes',
            'GetSupportType'
        ]

        for function_name in self._functions:
            self._support._FlagAsMethod(function_name)

    def AssignSupportToNode(self,NoNode:int,Support_type_ID:int):
        """
        Assigns the specified support to node(s).
        """
        self._support.AssignSupportToNode(NoNode,Support_type_ID)

    def CreateSupportFixed(self):
        """
        Creates a fully fixed support.
        """
        self._support.CreateSupportFixed()

    def CreateSupportPinned(self):
        """
        Creates a pinned support (i.e., free to rotate about local y and z axis, fixed in all other degrees of freedom).
        """
        self._support.CreateSupportPinned()

    def GetSupportCount(self):
        """
        Gets the total number of supported nodes exist in the current structure.
        """
        return (self._support.GetSupportCount())
    
    def GetSupportNodes(self):
        """
        Gets all supported nodes in an array.
        """
        n_supports = self._support.GetSupportCount()

        safe_list = make_safe_array_long(n_supports)
        lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

        self._support.GetSupportNodes(lista)

        return (lista[0])

    def GetSupportType(self,node:int):
        """
        Gets the support type for the specified node.
        """
        return self._support.GetSupportType(node)
    