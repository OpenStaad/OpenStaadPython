# OpenStaad

[![PyPI Downloads](https://static.pepy.tech/badge/openstaad)](https://pepy.tech/projects/openstaad)

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
from openstaad import Geometry, Root

geometry = Geometry()
root = Root()

# Function that returns a list
beam_list = geometry.GetBeamList()

# Function that retuns a string
file_name = root.GetSTAADFile()

# Function that recibe an argument
beam_number = 10 
beam_nodes = geometry.GetMemberIncidence(beam_number)


print(beam_list)
print(file_name)
print(beam_nodes)
```

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