from openstaad.tools import *
from comtypes import automation
from comtypes import client

class View():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._view = self._staad.View

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
    
