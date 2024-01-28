from comtypes import automation
from comtypes import client
import ctypes
from openstaad.file import _File
from openstaad.geometry import _Geometry
from openstaad.properties import _Properties
from openstaad.select import _Select
from openstaad.results import _Results
from openstaad.load import _Load


class Get():
    def __init__(self):
        
        self._os = client.GetActiveObject("StaadPro.OpenSTAAD")
        self.file = _File(self._os)
        self.geometry = _Geometry(self._os)
        self.properties = _Properties(self._os)
        self.select = _Select(self._os)
        self.results = _Results(self._os)
        self.load = _Load(self._os) 

    