from openstaad.Safe_variables import *
from comtypes import automation

class _Select():
    def __init__(self,os):
        self._os = os.Geometry
        self._view = os.View

        self._functions= [
            'SelectMultipleBeams'
        ]

        for function_name in self._functions:
            self._os._FlagAsMethod(function_name)

    ## PROPERTIES FUNCTIONS

    def SelectMultipleBeams(self,beam_list):
        for i in beam_list:
            self._os.SelectBeam(i)
        # self._view._FlagAsMethod('RefreshView')
        # self._view.RefreshView()
    
