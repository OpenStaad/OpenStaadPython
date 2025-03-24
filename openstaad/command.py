from openstaad.tools import *
from comtypes import automation
from comtypes import client

class Command():
    def __init__(self):
        self._staad = client.GetActiveObject("StaadPro.OpenSTAAD")
        self._command = self._staad.Command

        self._functions= [
           'PerformAnalysis',
        ]

        for function_name in self._functions:
            self._command._FlagAsMethod(function_name)

    def PerformAnalysis(self,print_option:int):
        """ 
        --> 1 - Print Load Data
        --> 2 - Print Statics Check
        --> 3 - Print Static Load
        --> 4 - Print Mode Shapes
        --> 5 - Print Both
        --> 6 - Print All
        --> 0 - No Print
        """
        self._command.PerformAnalysis(print_option)
