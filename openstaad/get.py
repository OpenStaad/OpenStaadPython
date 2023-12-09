from comtypes import automation
from comtypes import client
import ctypes
from openstaad.file import File
from openstaad.geometry import Geometry
from openstaad.properties import Properties


class Get():
    def __init__(self):
        
        self._os = client.GetActiveObject("StaadPro.OpenSTAAD")
        self.file = File(self._os)
        self.geometry = Geometry(self._os)
        self.properties = Properties(self._os)

    