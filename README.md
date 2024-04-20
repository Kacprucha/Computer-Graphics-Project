
# Elimination of covered elements
In this part of a project we crate a virtual camera that allows you to move around 2D plaines objects that you pass to the program and observe how the plaines covered each other. <br>
The Scan Line Algorithm was used to accomplish this task.

To see other part of a project you have to select correct brunch.

## Requirements
- Python 3.x
- Pygame
- NumPy

## Disclaimer
This part of an project was crated befor some changes were made to virtual camera it is based on so rotations in OX, OZ and using zoom can be problematic and in some cases it may cause irreversible changes on the plains. So as long as this paragraph is hear it means I didn't have time to correct it. Sorry.

## Usage
Run the program by executing main.py. <br>
Pass the paths to text files containing point coordinates as command-line arguments. Each text file should contain one point per line in the format: x y z. <br>
Example: <br>
```
300 100 20
210 40 100
160 90 100
200 200 40
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
