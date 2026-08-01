"""
_coerce.py — normalización de argumentos de la API pública de ops.

Traduce lo que escribe el usuario (int, entero de numpy, lista, tupla, range,
generador) a los tipos que espera la capa de marshalling, y rechaza de forma
ruidosa lo que no encaja.

La regla: **nunca aceptar en silencio algo que se vaya a malinterpretar del otro
lado del COM**. Un identificador mal pasado no produce un error de STAAD, produce
un modelo distinto del que el usuario cree haber construido.

Se usa `operator.index()` en vez de `isinstance(x, int)` porque acepta cualquier
objeto entero (`numpy.int64`, etc.) sin tener que enumerar tipos, y rechaza
floats y strings por su cuenta.

Nota de idioma: los docstrings van en español como el resto de `ops`, pero los
**mensajes de excepción van en inglés** — son superficie pública, y el README,
la documentación y los issues del paquete están en inglés. No traducirlos.
"""

import operator
from collections.abc import Iterable
from typing import Optional

__all__ = ["as_id", "as_id_list"]


def as_id(value, argname: str = "value", plural_hint: Optional[str] = None) -> int:
    """Un identificador entero (nodo, viga, placa…) a partir de cualquier entero.

    `plural_hint` es el nombre de la variante que sí acepta colecciones; si se
    da, pasar una secuencia produce un error que apunta directamente a ella.
    """
    if isinstance(value, bool):
        raise TypeError(f"{argname} expects an integer, not a bool")
    try:
        return operator.index(value)
    except TypeError:
        pass
    if plural_hint is not None and _is_collection(value):
        raise TypeError(
            f"{argname} expects a single integer; for several use {plural_hint}()"
        )
    raise TypeError(f"{argname} expects an integer, not {type(value).__name__}")


def as_id_list(values, argname: str = "value") -> list:
    """Lista de identificadores enteros a partir de un entero o de un iterable.

    Acepta tanto `5` como `[5, 6, 7]`, `(5, 6)`, `range(5, 9)` o un array de
    numpy. Devuelve siempre una lista de `int`.
    """
    if not isinstance(values, bool):
        try:
            return [operator.index(values)]
        except TypeError:
            pass
    # isinstance contra Iterable en vez de _is_collection: es la misma pregunta,
    # pero así el type checker sabe que lo que sigue es iterable.
    if isinstance(values, (str, bytes)) or not isinstance(values, Iterable):
        raise TypeError(
            f"{argname} expects an integer or a collection of integers, "
            f"not {type(values).__name__}"
        )
    # El índice va en el mensaje: en una lista larga, saber *cuál* elemento
    # falló es la diferencia entre corregirlo y tener que buscarlo a mano.
    return [as_id(v, f"{argname}[{i}]") for i, v in enumerate(values)]


def _is_collection(value) -> bool:
    """Iterable que no sea texto (un str es iterable, pero nunca es una lista de IDs)."""
    return isinstance(value, Iterable) and not isinstance(value, (str, bytes))
