# deVox
.inp (EMCoS Studio Voxel Text File) to .obj (Wavefront) converter.

This script converts to .obj file without the texture coordinates/normals. The faces are in quad mode.

## Installation

First, run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

And then clone the repository.
```bash
git clone git@github.com:memory-hunter/deVox.git
```

## Usage

```t
deVox.py [-h] -i INPUT

Convert a voxel file to an obj file.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input voxel file.
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
