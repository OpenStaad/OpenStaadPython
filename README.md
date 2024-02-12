# OpenStaad

## Abstract

This Python package is designed to facilitate the connection between the [OpenStaad API](https://docs.bentley.com/LiveContent/web/STAAD.Pro%20Help-v14/en/GUID-93E26CB6-E60E-4175-920A-72D504639722.html) and python. 

## Quick Info

- `openstaad` is a Python package to call easily functions from the OpenStaad API.
- MIT-License
- The intended audience is StaadPro users with knowledge of Python
- Compatibitity:
    - Tested with Python 3.10.9
    - Operating System: Windows 11  
- Dependencies:
    - [comtypes](https://pypi.org/project/comtypes/)

- See [implemented funcionts](docs/implemented.md) for a list of currently working features.
- Please contact the [developer](openstee611@gmail.com) for requests.

## Installation

Basic installation by pip.

    pip install openstaad

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

Not yet implemented

## Documentation

See [documentation](/docs/) folder 

## Contribution

The source code of *openstaad* can be found at __GitHub__, target your pull requests to the `main` branch:

https://github.com/OpenStaad/OpenStaadPython/pulls


## Feedback

Questions and feedback at __GitHub Discussions__:

https://github.com/OpenStaad/OpenStaadPython/discussions

Questions at __Stack Overflow__:

Post questions at [stack overflow](https://stackoverflow.com/) and use the tag `openstaad` or `openstaadpython`.

Issue tracker at __GitHub__: https://github.com/OpenStaad/OpenStaadPython/issues

## Contact

Please __always__ post questions at the [forum](https://github.com/OpenStaad/OpenStaadPython/discussions) 
or [stack overflow](https://stackoverflow.com/) to make answers 
available to other users as well. 

Feedback is greatly appreciated.

Konrad
