from comtypes import automation
from comtypes import client
import ctypes
from openstaad.file import File
from openstaad.geometry import Geometry
from openstaad.properties import Properties
from openstaad.select import Select
from openstaad.results import Results
from openstaad.load import Load


class Get():
    def __init__(self):
        
        self._os = client.GetActiveObject("StaadPro.OpenSTAAD")
        self.file = File(self._os)
        self.geometry = Geometry(self._os)
        self.properties = Properties(self._os)
        self.select = Select(self._os)
        self.results = Results(self._os)
        self.load = Load(self._os) 

    