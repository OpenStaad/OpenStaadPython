# Arquitectura `ops` de openstaad — documentación de lo implementado

> Registro de la nueva arquitectura `openstaad.ops`: qué se construyó, cómo, y qué queda
> pendiente/diferido. Reemplaza a los antiguos `ANALISIS_MIGRACION.md` y `AUDIT_OPS.md` (integrados aquí).
> Estado: **implementado y compilando**; validación funcional en Windows+STAAD.Pro pendiente.

---

## 1. Objetivo

Reorganizar `openstaad` para que:

- Se use con **un solo import**: `from openstaad import ops`.
- La API pública sea **plana**: todas las funciones cuelgan de la **sesión** (`s.GetBeamList()`),
  sin sub-namespaces por dominio ni por verbo.
- Todo gire alrededor de un objeto **`Session`** que administra la conexión COM.
- Sea legible para humanos e IA: nombres predecibles (PascalCase, espejo del oficial), docstrings, tipos.
- **Sin romper** a los usuarios actuales: la API vieja (`Root()`, `Geometry()`, …) sigue funcionando en
  paralelo, deprecada.

## 2. Origen

La implementación se portó desde el paquete **oficial de Bentley `openstaadpy`** (MIT, referencia local en
`openstaadpy/`, ignorado por git). Se replicó su **comportamiento** (marshalling y semántica), no su
estructura: el oficial es un módulo plano de funciones + errores tipados; aquí es una fachada `ops` sobre
una capa de marshalling propia (`bridge`), sin el sistema de errores del oficial (diferido).

## 3. Capas de la arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│  Capa 3 — Sesión / API plana  (from openstaad import ops)    │
│    s = ops.connect(filePath=None)  -> Session               │
│    s.GetBeamList()   s.GetNodeCoordinates(10)   s.Analyze()  │
│    (+ default de conveniencia: ops.GetBeamList())            │
├─────────────────────────────────────────────────────────────┤
│  Capa 2 — Módulos de dominio internos  (Root, Geometry, …)   │
│    Métodos alineados al oficial (PascalCase), sobre bridge   │
│    (organización interna; NO son API pública)                │
├─────────────────────────────────────────────────────────────┤
│  Capa 1 — bridge.py  (marshalling Python↔COM: ComVar)        │
├─────────────────────────────────────────────────────────────┤
│  comtypes / OpenSTAAD COM (STAAD.Pro, solo Windows)          │
└─────────────────────────────────────────────────────────────┘
```

## 4. La sesión (el corazón)

Un `Session` es dueño de: la **conexión COM** (una sola, compartida), el **`Bridge`** (una instancia,
con el gancho de errores), las **instancias de dominio internas** (a las que delega), la **superficie
plana** que ve el usuario, y el **ciclo de vida COM**.

### 4.1 `connect()` — único punto de entrada

```python
from openstaad import ops

# explícita (recomendada)
s = ops.connect(r"C:\models\torre.std")   # ruta -> ese .STD YA ABIERTO (moniker COM)
s = ops.connect()                          # sin args -> instancia activa
s.GetBeamList(); s.GetNodeCoordinates(10); s.Analyze()

# conveniencia (usa el default del módulo)
ops.connect(); ops.GetBeamList()

# varios modelos a la vez
a = ops.connect(r"C:\a.std"); b = ops.connect(r"C:\b.std")

# context manager (libera el COM al salir)
with ops.connect(path) as s:
    s.GetBeamList()
```

Firma: `connect(filePath=None, on_error=None) -> Session`.

### 4.2 Responsabilidades

| Tema | Comportamiento |
|---|---|
| **`filePath`** | Sube a `connect()` (único punto). **No abre** el archivo: se engancha a uno ya abierto. |
| **Retorno** | `connect()` devuelve un `Session` **y** lo guarda como default del módulo. |
| **Default de módulo** | `ops.<Func>()` son proxies al último `connect()`. Sin sesión → error claro *"no active session; call ops.connect() first"*. |
| **Varias sesiones** | Cada `connect()` es una sesión independiente; el default apunta a la última. |
| **Conexión compartida** | La sesión crea **una** conexión + **un** `Bridge` y los inyecta a los dominios. |
| **Superficie plana** | En construcción, la sesión **aplana** los métodos públicos de cada dominio como atributos propios (`_bind_flat`). |
| **Context manager** | `with ops.connect() as s:` → `s.close()` libera referencias COM. |
| **Errores** | La sesión posee el `Bridge(on_error=...)`. Hoy `on_error=None` (passthrough). |

### 4.3 Módulos de dominio: conexión inyectable

Cada dominio acepta conexión inyectada (la usa la sesión) o abre la suya (fallback standalone,
compatibilidad):

```python
class Geometry:
    def __init__(self, connection=None, bridge=None, filePath=None):
        # si no se inyectan -> standalone
```

## 5. La capa de marshalling: `bridge.py`

`Bridge` traduce Python↔COM (VARIANT/SAFEARRAY/BSTR). El handle **`ComVar`** es dueño de su buffer (evita
el bug de GC). Cubre las 8 formas reales del API:

- Salidas escalares: `out_int()`, `out_double()`.
- Strings: `out_str()` (estilo VARIANT*) y `out_bstr()` (estilo BSTR-byref).
- Arrays de salida: `out_int_array(n)`, `out_double_array(n)`, `out_str_array(n)`.
- Entradas: `in_value()`, `in_int/double/bool/str()`.
- Arrays de entrada: `in_*_array()` (crudo) y `in_*_array_variant()` (envuelto, con ownership).
- ctypes crudos: `c_int/c_double/...`, `byref()`.
- Gancho de errores: `check(retval)` (delega en `on_error`; passthrough por defecto).

## 6. Módulos de dominio portados (10, 729 métodos)

| Dominio | Métodos | | Dominio | Métodos |
|---|---:|---|---|---:|
| `property` | 206 | | `output` | 72 |
| `geometry` | 138 | | `view` | 67 |
| `load` | 131 | | `support` | 35 |
| `root` | 33 | | `table` | 24 (nuevo) |
| `command` | 17 | | `design` | 6 |

Todos alineados al comportamiento del oficial; envoltura de entradas **método a método** según el oficial;
sin `raise` de errores (diferido).

## 7. Estructura de archivos

```
openstaad/
  __init__.py          # API vieja + wrapper de deprecación (FutureWarning)
  root.py  geometry.py  load.py  output.py  properties.py   # --- API vieja, intacta ---
  view.py  support.py  command.py  design.py  tools.py
  ops/                 # === arquitectura nueva ===
    __init__.py        # fachada: connect() -> Session, default de módulo, proxies
    session.py         # class Session (conexión, bridge, aplanado, ciclo de vida)
    _com.py            # acquire(filePath): conexión COM (activa o por ruta)
    bridge.py          # marshalling (ComVar)
    root.py  geometry.py  load.py  output.py  property.py  view.py
    support.py  command.py  design.py  table.py
```

- **Sin choque de nombres**: `openstaad.root.Root` (viejo) vs `openstaad.ops.root.Root` (nuevo).
- Se importa con `from openstaad import ops`.

## 8. Convenciones de nombres

- **PascalCase en todo**: interno y público usan el nombre del oficial (`GetBeamList`) → diffs triviales
  con futuras versiones de Bentley, cero rename.
- **snake_case: diferido** (junto con la "materialización" — ver §12).
- **Unicidad**: al ser plano, los nombres deben ser globalmente únicos. Solo hay **1 colisión** en 729:
  `RemoveAttribute` (en `load` y `property`) — ver §10.

## 9. Manejo de errores

- `bridge.Bridge(on_error=...)` es el gancho único; lo configura la sesión.
- **Hoy `on_error=None`** (passthrough): se omitieron los `raise_os_error_if_error_code` del oficial. La
  política propia se diseñará después y se inyecta en `ops.connect(on_error=...)`, aplicando a todo.
- El catálogo de códigos del oficial (`oserrors.py`) queda como referencia, no se copió.

## 10. Auditoría (resultado y issues conocidos)

Se auditaron los 729 métodos contra el oficial en 6 dimensiones automáticas (cobertura, aridad, método COM,
nº de args, tamaños de array, envoltura de entradas, estilo de string). **Estructura: sin desajustes.**
Hallazgos de comportamiento:

**Bugs del oficial CORREGIDOS (divergencia deliberada)** — en `load.py`:
- `AddSeismicDefSelfWeight`: llamaba a `AddSeismicDefMemberWeight` → corregido a `AddSeismicDefSelfWeight`.
- `GetConcMoments`: usaba `GetConcForceCount`/`GetConcForces` → corregido a los de momento.
- `GetElementConcLoads`: dimensionaba con `GetElementPressureLoadCount` → corregido a `GetElementConcLoadCount`.
- `GetNotionalLoadByIndex`: llamaba a `GetElementLoadInfo` → corregido a `GetNotionalLoadByIndex`.
  **⚠️ orden/tipos de out-params sin verificar contra la firma COM real — confirmar en Windows** (marcado en el código).

**Bugs del oficial que también se arreglaron de facto**:
- `output.GetResultantForceAlongLineForPlateList`: el oficial envolvía el array en una lista →
  `addressof(list)` crashea; aquí se usa `out_double_array(6)`.
- `property.GetElementListByAttribute`: el oficial usaba tag escalar `VT_I4` para un array; aquí se usa el
  tag de array correcto.

**Issues conocidos a decidir/probar**:
- **Colisión `RemoveAttribute`**: gana `load` (registrado antes que `property` en `session._DOMAINS`); el de
  `property` queda accesible vía `s._property.RemoveAttribute` y registrado en `session._collisions`. La
  firma difiere → llamar el plano con args de property da `TypeError`.
- **Retorno `list` vs `tuple`**: `ComVar.value` siempre devuelve `list` donde el oficial a veces devolvía
  `tuple`. Bajo impacto.
- **Riesgo residual**: el audit valida *cantidad* de args del dispatch COM, no el *orden*. Priorizar en el
  humo los métodos multi-arg (`GetParametricSurfaceInfoEx`, los `AddUPTProperty*`) y los getters de string.

## 11. Compatibilidad y deprecación

- **Convivencia**: API vieja + `ops` en paralelo. La API vieja es **aditivamente** deprecada, no rota.
- **Aviso**: `openstaad/__init__.py` envuelve el `__init__` de las 9 clases viejas con un `FutureWarning`
  (visible por defecto) que indica el reemplazo, la versión de remoción (**0.1.0**) y la URL de la guía
  (`_MIGRATION_URL`). No cambia tipos (sin subclases).
- **Guía de migración**: `docs/migration_guide.md` (para publicar en la web) documenta lo deprecado, los
  3 renombres, el método eliminado (`IsRelease`), los cambios de comportamiento, y un prompt de migración
  para LLM con pre-flight de entorno.
- **Plan de versiones (SemVer 0.x)**: deprecar en `0.0.x` (ahora) → eliminar la API vieja en `0.1.0`.

## 12. Estado de validación y pendientes

**Validado**: `py_compile` de todo el paquete (viejo + `ops`); empaquetado (el wheel incluye `ops/`);
pruebas iniciales del usuario en Windows funcionan.

**Pendiente / diferido**:
- **Humo en Windows+STAAD.Pro** por módulo (nada se ejecutó en el entorno de desarrollo, macOS sin comtypes).
  Foco: quirks corregidos C1–C4 (sobre todo `GetNotionalLoadByIndex`), orden de args en multi-arg, encoding
  de strings, colisión `RemoveAttribute`.
- **CI en `windows-latest`**: equivalencia `bridge` vs oficial (comtypes real, sin STAAD).
- **Manejo de errores propio** (política inyectada en `on_error`).
- **snake_case + materialización** de la superficie plana (codegen de `.py` reales o stubs `.pyi`).
