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

    def GetSupportType(self,node:int):
        """
        Gets the support type for the specified node.
        """
        return self._support.GetSupportType(node)
    