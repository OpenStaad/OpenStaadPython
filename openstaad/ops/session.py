"""
session.py — la Session: el corazón de la API ops.

Una Session es dueña de:
  - la conexión COM (una sola, compartida),
  - el Bridge (uno solo) y con él la política de errores,
  - las instancias de dominio internas (Root, Geometry, …),
  - la superficie plana en PascalCase que ve el usuario (s.GetBeamList()).

Los métodos de cada dominio se "aplanan" sobre la sesión: se enlazan directamente
como atributos, de modo que `s.GetSTAADFile()` llama al método del dominio Root.
"""

import inspect

from .bridge import Bridge
from ._com import acquire
from .root import Root
from .design import Design
from .command import Command
from .support import Support
from .view import View
from .table import Table
from .output import Output
from .geometry import Geometry
from .load import Load
from .property import Property

# Registro de dominios: (atributo interno, clase). Los 10 dominios del oficial.
_DOMAINS = [
    ("_root", Root),
    ("_design", Design),
    ("_command", Command),
    ("_support", Support),
    ("_view", View),
    ("_table", Table),
    ("_output", Output),
    ("_geometry", Geometry),
    ("_load", Load),
    ("_property", Property),
]


def _public_methods(cls):
    """Nombres de métodos públicos (no _-prefijados) definidos en la clase."""
    for name, _member in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not name.startswith("_"):
            yield name


class Session:
    """Sesión de conexión a un modelo de STAAD.Pro.

    Se crea con `ops.connect(...)`. Expone la superficie plana de toda la API.
    """

    def __init__(self, filePath: str = None, on_error=None):
        # Una conexión COM y un Bridge, compartidos por todos los dominios.
        self._staad = acquire(filePath)
        self._bridge = Bridge(on_error=on_error)

        self._collisions = {}  # nombre -> lista de dominios que lo definen
        self._flat = set()     # nombres ya enlazados en plano

        for attr, cls in _DOMAINS:
            instance = cls(connection=self._staad, bridge=self._bridge)
            setattr(self, attr, instance)
            self._bind_flat(instance)

    def _bind_flat(self, instance):
        """Enlaza los métodos públicos del dominio directamente sobre la sesión."""
        for name in _public_methods(type(instance)):
            if name in self._flat:
                # Colisión global (p.ej. RemoveAttribute): se registra para
                # desambiguar puntualmente; por ahora gana el primero.
                self._collisions.setdefault(name, []).append(type(instance).__name__)
                continue
            setattr(self, name, getattr(instance, name))
            self._flat.add(name)

    # ------------------------------------------------------------------ #
    # Ciclo de vida
    # ------------------------------------------------------------------ #
    def close(self):
        """Libera las referencias COM de la sesión.

        No llama a CoUninitialize para no afectar a otras sesiones del mismo hilo.
        """
        self._staad = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False
