"""
openstaad.ops — API nueva de openstaad.

Uso:

    from openstaad import ops

    # explícito (recomendado)
    s = ops.connect(r"C:\\models\\torre.std")   # o ops.connect() para la activa
    s.GetSTAADFile()
    s.GetApplicationVersion()

    # conveniencia (usa el default del módulo)
    ops.connect()
    ops.GetSTAADFile()

    # varios modelos a la vez
    a = ops.connect(r"C:\\a.std")
    b = ops.connect(r"C:\\b.std")

    # context manager (libera el COM al salir)
    with ops.connect(path) as s:
        s.GetSTAADFile()

La API pública es **plana**: todas las funciones cuelgan de la sesión (PascalCase,
espejo del oficial). El paso a snake_case está diferido.
"""

from .session import Session

__all__ = ["connect", "current_session", "Session"]

# Última sesión creada; respaldo de los proxies de conveniencia a nivel de módulo.
_default = None


def connect(filePath: str = None, on_error=None) -> Session:
    """Conecta a STAAD.Pro y devuelve una `Session`.

    filePath None -> instancia activa; filePath dado -> ese .STD ya abierto.
    La sesión devuelta se guarda además como default del módulo para `ops.<Func>()`.
    """
    global _default
    session = Session(filePath=filePath, on_error=on_error)
    _default = session
    return session


def current_session() -> Session:
    """La sesión default actual (o None si no se ha llamado a connect())."""
    return _default


def __getattr__(name):
    """Proxy de conveniencia: `ops.GetSTAADFile()` -> sesión default.

    Solo se invoca cuando el atributo no existe a nivel de módulo (PEP 562).
    """
    if _default is None:
        raise RuntimeError("no active session; call ops.connect() first")
    try:
        return getattr(_default, name)
    except AttributeError:
        raise AttributeError(f"module 'openstaad.ops' has no attribute {name!r}") from None
