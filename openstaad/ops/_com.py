"""
_com.py — utilidades de conexión COM compartidas por el subpaquete ops.

`acquire()` centraliza la lógica que antes repetía cada clase: conectar a la
instancia activa de STAAD.Pro o a un archivo .STD ya abierto (por su ruta).
"""

from comtypes import client, CoInitialize, COMError
import os


def acquire(filePath: str = None):
    """Devuelve el objeto COM raíz de OpenSTAAD.

    - filePath None  -> instancia activa (`GetActiveObject`).
    - filePath dado  -> ese archivo YA ABIERTO (`CoGetObject` por moniker).

    No abre el archivo: se engancha a uno abierto en una instancia en ejecución.
    """
    CoInitialize()
    try:
        if filePath:
            filePath = os.path.abspath(filePath)
            if not os.path.exists(filePath):
                raise FileNotFoundError(filePath)
            return client.CoGetObject(filePath, dynamic=True)
        return client.GetActiveObject("StaadPro.OpenSTAAD")
    except COMError:
        raise RuntimeError("Cannot connect to STAAD.Pro")
