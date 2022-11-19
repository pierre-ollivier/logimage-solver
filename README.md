# logimage-solver

Welcome to the logimage-solver project! This project follows one objective:
Allow the user to enter an image and a preferred logimage size, and get as output a solvable logimage (a logimage that has exactly one solution, and neither zero nor multiple).

Currently, the project is in development state, so the modules are not totally connected to each other.
Furthermore, the development of this project is stopped because it is being merged (and improved) with another project.

- Run `mainwindow.py`, that will display a window. You can then upload an image, choose the number of rows and columns, choose the threshold for black and white conversion, and generate the logimage in a new window. There is no guarantee that the logimage has only one solution, however it has at least one. The graphical output is only adapted to squared logimages and squared input images, rectangular (non-squared) images and logimages won't raise any error but the output might look strange.
- Run `main.py`, that will perform a speed benchmark on the logimage-solving algorithm.

Inside the project, the logimages are handled using two types (classes):
- `Logimage`: it contains the constraints (the numbers on the top and left of a printed logimage). Constraints are represented in two lists: `top_constraints` and `left_constraints`. For each row or column, the corresponding left/top constraint is a list of integers.
- `Board`: it contains the state of the logimage grid (whether a square is marked as black, marked as white or unknown). The data is represented as a numpy matrix, and the values used to represent the data are the following:
- `1` for a black square
- `0` for a white square
- `-1` for an uncertain square.
A `Board` object is initialized with all squares being equal to -1.
The `Board` class provides a method `draw()` that draws the board (without the constraints) in the console.

Ideas for the next steps:
- Check, within reasonable time, if the solution to a Logimage is unique (this may be reached by randomly solving a Logimage n times, and see if the obtained solutions are the same).
- If the logimage has multiple solutions, give the user an advice to slightly adjust the dimensions of the logimage, the black/white threshold, or even the data itself to have only one solution remaining.
- Allow the user to draw himself the logimage on a grid, while checking the existence and the uniqueness of a solution.
