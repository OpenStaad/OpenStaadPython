from .root import Root
from .geometry import Geometry
from .load import Load
from .output import Output
from .properties import Properties
from .view import View
from .design import Design
from .command import Command
from .support import Support

# --- Aviso de deprecación de la API antigua (clases sueltas) ---------------
# La nueva API es `from openstaad import ops` + `ops.connect()`. Las clases
# antiguas siguen funcionando durante la transición, pero avisan al instanciarse.
# Se usa FutureWarning (visible por defecto) para que lo vea el usuario final.
import functools as _functools
import warnings as _warnings

# Guía de migración (editar aquí si cambia la URL).
_MIGRATION_URL = "https://www.openstaad.com/docs/migration_guide"


def _deprecate_legacy(cls):
    _orig_init = cls.__init__

    @_functools.wraps(_orig_init)
    def __init__(self, *args, **kwargs):
        _warnings.warn(
            f"openstaad.{cls.__name__} (legacy API) is deprecated and will be removed in "
            "version 0.1.0; use `from openstaad import ops` and `ops.connect()` instead. "
            f"Migration guide: {_MIGRATION_URL}",
            FutureWarning,
            stacklevel=2,
        )
        _orig_init(self, *args, **kwargs)

    cls.__init__ = __init__
    return cls


for _cls in (Root, Geometry, Load, Output, Properties, View, Design, Command, Support):
    _deprecate_legacy(_cls)
