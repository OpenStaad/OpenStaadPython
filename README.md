# OpenStaad

[![PyPI Downloads](https://static.pepy.tech/badge/openstaad)](https://pepy.tech/projects/openstaad)

> [!WARNING]
> **The class-based API is deprecated.** The standalone classes (`Root()`, `Geometry()`,
> `Load()`, `Output()`, `Properties()`, `View()`, `Design()`, `Command()`, `Support()`) are
> deprecated in the `0.0.x` releases and **will be removed in `0.1.0`**. Instantiating any of
> them now emits a `FutureWarning`. Use the new single-import session API instead:
> `from openstaad import ops` → `ops.connect()`. See [Migration](#migration) below, or the full
> [migration guide](https://www.openstaad.com/docs/migration_guide).

## Abstract

openstaad python is a starting project to wrap the official OpenStaad API functionalities into a Python package.

It aims to facilitate the connection between StaadPRO and Python, avoiding boilerplate code and type management, allowing the user to focus on the real automation tasks.

## Quick Info

- `openstaad` is a Python package to call easily functions from the OpenStaad API.
- Require a StaadPRO and a valid file open to connect
- MIT-License
- The intended audience is StaadPro users with knowledge of Python
- Compatibitity:
    - Tested with Python 3.10.9
    - Operating System: Windows 11  
- Dependencies:
    - [comtypes](https://pypi.org/project/comtypes/)

## Installation

Basic installation by pip.

```bash 
pip install openstaad
```

## A simple example

For the next example, a valid STAAD.Pro file should be open.

```Python
from openstaad import ops

# Connect to the running STAAD.Pro session (a valid .STD file must be open)
s = ops.connect()

# Function that returns a list
beam_list = s.GetBeamList()

# Function that returns a string
file_name = s.GetSTAADFile()

# Function that receives an argument
beam_number = 10
beam_nodes = s.GetMemberIncidence(beam_number)

print(beam_list)
print(file_name)
print(beam_nodes)
```

## Migration

The class-based API is deprecated and will be removed in `0.1.0`. Migrating is almost entirely
mechanical: **method names stay the same** — you just consolidate the per-domain instances
(`Geometry()`, `Root()`, …) into a single session object returned by `ops.connect()` and route
every call through it.

```Python
# Legacy (deprecated)
from openstaad import Geometry, Root
geometry = Geometry()
root = Root()
beams = geometry.GetBeamList()

# New
from openstaad import ops
s = ops.connect()
beams = s.GetBeamList()
```

A few methods need manual attention:

**Renamed**

- `GetElementGlobalOffset` → `GetElementGlobalOffSet`
- `GetElementOffsetSpec` → `GetElementOffSetSpec`
- `AddResponseSpectrumLoadEx` → `AddResponseSpectrumLoad` (signature also changes: `data_pairs` moves to the last argument)

**Removed**

- `IsRelease()` — no direct replacement; call `GetMemberReleaseSpecEx()` and evaluate the result yourself.

**Same name, different result (behavior changes)**

- Coordinates and lengths are no longer rounded to 3 decimals — full precision is returned.
- `GetApplicationVersion` no longer includes the `"Version "` prefix.
- `GetAnalysisStatus` dict key `"CPUTime(sec)"` is now `"CPUTime"`.
- `NewSTAADFile` no longer creates subfolders and now requires three arguments.
- `SaveModel` parameter changed from `silent: int` to `saveSilent: bool`.

Full guide: <https://www.openstaad.com/docs/migration_guide>.

## Website

[www.openstaad.com](https://www.openstaad.com/)

## Contribution

The source code of *openstaad* can be found at __GitHub__, target your pull requests to the `main` branch:

https://github.com/OpenStaad/OpenStaadPython/pulls


## Feedback

Questions and feedback at __GitHub Discussions__:
https://github.com/OpenStaad/OpenStaadPython/discussions

Issue tracker at __GitHub__:
https://github.com/OpenStaad/OpenStaadPython/issues

## Contact

Please __always__ post questions at the [forum](https://github.com/OpenStaad/OpenStaadPython/discussions) 
 to make answers available to other users as well. 

Feedback is greatly appreciated.

Konrad