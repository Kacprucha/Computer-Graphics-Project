# Virtual Camera
In this part of a project we crate a virtual camera that allows you to move around 3D objects that you pass to the program.

To see other part of a project you have to select correct brunch.

## Requirements
- Python 3.x
- Pygame
- NumPy

## Usage
Run the program by executing main.py. <br>
Pass the paths to text files containing point coordinates as command-line arguments. Each text file should contain one point per line in the format: x y z. <br>
Example: <br>
```
-125 -125 0
-25 -125 0
-25 -25 0
-125 -25 0
-125 -125 100
-25 -125 100
-25 -25 100
-125 -25 100
```
Use the following controls to interact with the visualization: <br>
### Movment of camera
| Key | Direction |
| ------------- | ------------- |
| W  | Up  |
| S  | Dwon  |
| A | Right |
| D | Left |
| Arrow Up | Forward |
| Arrow Down | Backward |

### Rotations
| Key | Direction |
| ------------- | ------------- |
| Q  | Left rotation on OX  |
| E  | Right rotation on OX  |
| Z | Left rotation on OY |
| C | Right rotation on OY |
| Arrow Left | Left rotation on OZ |
| Arrow Right | Right rotation on OZ |

### Zoom
| Key | Direction |
| ------------- | ------------- |
| P  | Zoom in  |
| M  | Zoom out  |

