"""
bridge.py — puente de marshalling entre Python y COM (STAAD.Pro / OpenSTAAD).

Traduce datos entre el mundo Python y el mundo COM (VARIANT / SAFEARRAY / BSTR)
en las dos direcciones:

  - out_* : reserva un buffer y lo prepara para recibir un parámetro de *salida*;
            luego se lee con `.value`.
  - in_*  : envuelve un valor Python como VARIANT/SAFEARRAY para pasarlo como
            argumento de *entrada* a un método COM.

Formas de marshalling reales que aparecen en OpenSTAAD (todas cubiertas aquí):

  1. Escalar out VT_R8 / VT_I4                     -> out_double / out_int
  2. String out vía VARIANT(c_char_p, VT_BSTR)     -> out_str
  3. String out vía BSTR + ctypes.byref            -> out_bstr
  4. Array out (fijo o dimensionado por un count)  -> out_*_array(size)
  5. Escalar de entrada (raw o VARIANT)            -> in_value / in_int / ...
  6. Array de entrada como SAFEARRAY crudo         -> in_int_array / in_double_array
  7. Array de entrada envuelto en VARIANT byref    -> in_int_array_variant / ...
  8. ctype crudo + ctypes.byref                    -> c_int / c_double / ... + byref

Diseño en dos capas (a propósito, para poder testear cada una por separado):

  - Capa primitiva  -> `_safe_array` / `_byref`: crean el buffer y el VARIANT
    crudo. Equivalente byte-a-byte a `make_safe_array_*` + `make_variant_vt_ref`.
  - Capa conveniencia -> métodos `out_*` / `in_*` y `ComVar.value`: lectura tipada,
    redondeo opcional y guarda de lista vacía. No existen en la capa primitiva y no
    deben compararse contra ella.
"""

import ctypes
from comtypes import automation

__all__ = ["Bridge", "ComVar"]


class ComVar:
    """Una variable COM que es *dueña* de su backing buffer.

    Mientras el handle viva, el puntero que COM guarda hacia el buffer no queda
    colgando (evita el bug de GC que el enfoque de funciones sueltas deja como
    responsabilidad implícita de quien llama). Sirve para:

      - salidas (out_*): se pasa `.ref` al método COM y luego se lee `.value`.
      - entradas-array envueltas en VARIANT (in_*_array_variant): se pasa `.ref`;
        si el método es in/out, `.value` devuelve el array de vuelta.

    `ref`   -> lo que se pasa a COM (un VARIANT byref, o un `ctypes.byref`).
    `value` -> desempaqueta el resultado a un tipo Python.
    """

    __slots__ = ("_buffer", "ref", "_read")

    def __init__(self, buffer, ref, read):
        self._buffer = buffer          # se mantiene vivo mientras viva el handle
        self.ref = ref                 # esto es lo que se pasa a COM
        self._read = read              # closure sin argumentos que lee el resultado

    @property
    def value(self):
        return self._read()


class Bridge:
    """Administra la creación de variables COM (entrada y salida).

    Uso típico (una instancia por método):

        b = Bridge()
        x, y, z = b.out_double(), b.out_double(), b.out_double()
        geometry.GetNodeCoordinates(node, x.ref, y.ref, z.ref)
        return x.value, y.value, z.value

    El parámetro `on_error` es el gancho para tu política de errores propia: una
    función `on_error(retval)` que decide qué hacer con el código de retorno de
    OpenSTAAD. Sin él, `check()` es un passthrough y no impone ninguna filosofía.
    """

    def __init__(self, on_error=None):
        self._on_error = on_error

    # ------------------------------------------------------------------ #
    # Capa primitiva (equivalente a make_safe_array_* + make_variant_vt_ref)
    # ------------------------------------------------------------------ #
    @staticmethod
    def _safe_array(ctype, size):
        return automation._midlSAFEARRAY(ctype).create([0] * size)

    @staticmethod
    def _safe_array_input(ctype, seq):
        return automation._midlSAFEARRAY(ctype).create(list(seq))

    @staticmethod
    def _byref(buffer, tag):
        var = automation.VARIANT()
        var._.c_void_p = ctypes.addressof(buffer)
        var.vt = tag | automation.VT_BYREF
        return var

    @staticmethod
    def _empty_variant():
        var = automation.VARIANT()
        var.vt = automation.VT_EMPTY
        return var

    # ------------------------------------------------------------------ #
    # Salidas escalares
    # ------------------------------------------------------------------ #
    def out_int(self):
        """Salida entera (VT_I4)."""
        buf = self._safe_array(ctypes.c_long, 1)
        var = self._byref(buf, automation.VT_I4)
        return ComVar(buf, var, lambda: var[0])

    def out_double(self, ndigits=None):
        """Salida flotante (VT_R8).

        Si se pasa `ndigits`, `.value` redondea a esa cantidad de decimales
        (comodidad; la capa primitiva nunca redondea).
        """
        buf = self._safe_array(ctypes.c_double, 1)
        var = self._byref(buf, automation.VT_R8)
        if ndigits is None:
            read = lambda: var[0]
        else:
            read = lambda: round(var[0], ndigits)
        return ComVar(buf, var, read)

    def out_str(self):
        """Salida de texto estilo `VARIANT*` (c_char_p + VARIANT VT_BSTR, leer [0])."""
        buf = automation.c_char_p()
        var = self._byref(buf, automation.VT_BSTR)
        return ComVar(buf, var, lambda: var[0])

    def out_bstr(self):
        """Salida de texto estilo `BSTR*` (BSTR + ctypes.byref, leer .value).

        Convenio distinto de out_str: lo usan las firmas COM declaradas como
        `BSTR*` en vez de `VARIANT*` (frecuente en el módulo de resultados/output).
        """
        buf = automation.BSTR("")
        return ComVar(buf, ctypes.byref(buf), lambda: buf.value)

    # ------------------------------------------------------------------ #
    # Salidas de array
    # ------------------------------------------------------------------ #
    def out_int_array(self, size):
        """Salida array de enteros (VT_ARRAY | VT_I4). `.value` -> list."""
        buf = self._safe_array(ctypes.c_long, size)
        var = self._byref(buf, automation.VT_ARRAY | automation.VT_I4)
        return ComVar(buf, var, lambda: list(var[0]))

    def out_double_array(self, size):
        """Salida array de flotantes (VT_ARRAY | VT_R8). `.value` -> list."""
        buf = self._safe_array(ctypes.c_double, size)
        var = self._byref(buf, automation.VT_ARRAY | automation.VT_R8)
        return ComVar(buf, var, lambda: list(var[0]))

    def out_str_array(self, size):
        """Salida array de textos (VT_ARRAY | VT_BSTR). `.value` -> list."""
        buf = automation._midlSAFEARRAY(automation.BSTR).create([""] * size)
        var = self._byref(buf, automation.VT_ARRAY | automation.VT_BSTR)
        return ComVar(buf, var, lambda: list(var[0]))

    # ------------------------------------------------------------------ #
    # Entradas: envolver un valor Python como VARIANT
    # ------------------------------------------------------------------ #
    def in_value(self, value=None):
        """Entrada autotipada: deja que comtypes elija el VT según el valor."""
        var = automation.VARIANT()
        if value is not None:
            var.value = value
        return var

    def in_int(self, value):
        return automation.VARIANT(value, automation.VT_BYREF | automation.VT_I4)

    def in_double(self, value):
        return automation.VARIANT(value, automation.VT_BYREF | automation.VT_R8)

    def in_bool(self, value):
        return automation.VARIANT(value, automation.VT_BYREF | automation.VT_BOOL)

    def in_str(self, value):
        return automation.VARIANT(value, automation.VT_BYREF | automation.VT_BSTR)

    def bstr(self, value=""):
        """Un BSTR crudo (útil para armar entradas manualmente)."""
        return automation.BSTR(value)

    # ------------------------------------------------------------------ #
    # Entradas de array como SAFEARRAY crudo (guarda de vacío -> VT_EMPTY)
    # ------------------------------------------------------------------ #
    def _in_array(self, seq, ctype):
        if not seq:
            return self._empty_variant()
        return self._safe_array_input(ctype, seq)

    def in_int_array(self, seq):
        return self._in_array(seq, ctypes.c_long)

    def in_double_array(self, seq):
        return self._in_array(seq, ctypes.c_double)

    def in_str_array(self, seq):
        if not seq:
            return self._empty_variant()
        return automation._midlSAFEARRAY(automation.BSTR).create(list(seq))

    # ------------------------------------------------------------------ #
    # Entradas de array envueltas en VARIANT byref (VT_ARRAY | ...)
    # Devuelven un ComVar dueño del buffer -> el puntero no queda colgando.
    # Si el método COM es in/out, `.value` devuelve el array de vuelta.
    # ------------------------------------------------------------------ #
    def _in_array_variant(self, seq, ctype, elem_tag):
        if not seq:
            return ComVar(None, self._empty_variant(), lambda: [])
        buf = self._safe_array_input(ctype, seq)
        var = self._byref(buf, automation.VT_ARRAY | elem_tag)
        return ComVar(buf, var, lambda: list(var[0]))

    def in_int_array_variant(self, seq):
        return self._in_array_variant(seq, ctypes.c_long, automation.VT_I4)

    def in_double_array_variant(self, seq):
        return self._in_array_variant(seq, ctypes.c_double, automation.VT_R8)

    # ------------------------------------------------------------------ #
    # ctypes crudos + byref (para firmas que no usan VARIANT)
    # ------------------------------------------------------------------ #
    def c_int(self, value=0):
        return ctypes.c_int(value)

    def c_float(self, value=0.0):
        return ctypes.c_float(value)

    def c_double(self, value=0.0):
        return ctypes.c_double(value)

    def c_bool(self, value=False):
        return ctypes.c_bool(value)

    def byref(self, obj):
        return ctypes.byref(obj)

    # ------------------------------------------------------------------ #
    # Gancho de errores (política inyectable; passthrough por defecto)
    # ------------------------------------------------------------------ #
    def check(self, retval):
        """Punto único para tu política de errores.

        Si se inyectó `on_error`, delega la decisión (qué código es error, qué
        excepción lanzar) en él. Sin handler, devuelve `retval` tal cual: bridge
        no impone ninguna filosofía de errores.
        """
        if self._on_error is not None:
            return self._on_error(retval)
        return retval
