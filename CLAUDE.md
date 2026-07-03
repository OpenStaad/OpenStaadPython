# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`openstaad` is a Python package that wraps the **OpenSTAAD COM API** of Bentley STAAD.Pro. It exists to hide the ctypes/COM boilerplate (SAFEARRAY marshalling, `VARIANT` by-ref out-parameters, type juggling) so users write plain Python.

Hard constraints that shape everything:
- **Windows-only at runtime.** It talks to a running STAAD.Pro instance over COM (`comtypes`). It cannot connect — and most code cannot be exercised — without STAAD.Pro installed *and a `.STD` model open*. This dev machine is macOS, so runtime testing is not possible here; validate logic by reading, not by running.
- No test framework and no CI tests. `test.py` and `examples/*.py` are manual smoke scripts that require a live STAAD.Pro session.

## Architecture

The package is a set of façade classes, one per OpenSTAAD sub-object, all in `openstaad/` and re-exported from `openstaad/__init__.py`:

`Root` (top-level app), `Geometry`, `Load`, `Output`, `Properties`, `Command`, `View`, `Design`, `Support`.

Every class follows the **same construction pattern** (see `openstaad/root.py`, `openstaad/geometry.py`):

1. `CoInitialize()`, then connect: `client.GetActiveObject("StaadPro.OpenSTAAD")` for the active session, or `client.CoGetObject(filePath, dynamic=True)` when a `filePath` is passed to the constructor. A `COMError` is re-raised as `RuntimeError("Cannot connect to STAAD.Pro")`.
2. Grab the relevant COM sub-object (e.g. `root_com.Geometry`) into `self._geometry` / `self._root` / etc. (`Root` keeps the top object itself.)
3. Iterate a hardcoded `self._functions` list of COM method names and call `_FlagAsMethod(name)` on each — **comtypes requires this before a COM member can be invoked as a method.**
4. `__getattr__` delegates any unknown attribute to the underlying COM object, so unwrapped API calls still pass through (untyped, raw).

**`openstaad/tools.py`** holds the marshalling helpers shared by every module (`from openstaad.tools import *`). Two roles:
- `make_safe_array_*` build `comtypes` SAFEARRAYs of a given size/type.
- `make_variant_vt_ref` / `make_safe_bstr` wrap them in a `VARIANT` with `VT_BYREF` so the COM method can write into them (OpenSTAAD returns most data through out-parameters, not return values).

**The idiom for wrapping an out-parameter method** (this is the core thing to learn): allocate a safe array, wrap it in a by-ref variant, pass the variant to the COM call, then read the result back from `variant[0]`. Scalars use size-0/1 arrays with `VT_I4`/`VT_R8`; collections size the array from a prior count call and use `VT_ARRAY | VT_I4`. Examples: `Geometry.GetNodeCoordinates` (three double out-params) and `Geometry.GetNodeList` (array sized by `GetNodeCount()`). Length/coordinate results are commonly rounded to 3 decimals (`round(v*1000)/1000`).

When adding a new wrapped function: add its name to the class's `self._functions` list (so it gets `_FlagAsMethod`'d) and write the method using the out-parameter idiom above.

## Common commands

```bash
# Dev env (on Windows the venv activate script lives at venv/Scripts/activate)
python -m venv venv
pip install -r requirements.txt        # comtypes==1.4.15

# Build the distribution (hatchling backend)
python -m build

# Manual smoke test — ONLY works on Windows with STAAD.Pro open
python test.py
```

## Releasing

Publishing to PyPI is driven entirely by pushing a git tag (`.github/workflows/release.yaml`), which builds and publishes via trusted publishing. Steps:

1. Bump `version` in `pyproject.toml` (this is manual and separate — the tag does not set it).
2. `git tag 0.0.x` then `git push origin --tags`.

Tag format must match the workflow's regex: `X.Y.Z` optionally with an `aN` / `bN` / `rcN` suffix (e.g. `0.0.13`, `0.0.13a2`).

> Gotcha: `release.yaml` still has placeholder `env` values (`PACKAGE_NAME: "<PACKAGE_NAME>"` etc.). The `check_pypi` job reads `env.PACKAGE_NAME`, so that job queries the wrong PyPI URL until the placeholders are filled in.
