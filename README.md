# Rubix Cube Solver

## Overview
Rubix Cube Solver is a project designed to solve a Rubik's Cube by allowing users to input the faces of the cube using OpenCV. The project then applies the Kociemba algorithm to compute the solution, returning the sequence of moves required to solve the cube.

## Features
- **Face Detection**: Use OpenCV to capture and recognize the faces of the Rubik's Cube.
- **Kociemba Algorithm**: Apply the Kociemba algorithm to find the optimal solution for solving the cube.
- **Solution Output**: Display the sequence of moves needed to solve the cube.

## Installation

### Prerequisites
- Python 3.x
- OpenCV
- Kociemba

## Usage

1. Run the main script to start the Rubik's Cube solver:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to capture each face of the Rubik's Cube using your webcam.

3. Once all faces are captured, the Kociemba algorithm will process the input and return the solution.

4. The solution will be displayed as a sequence of moves to solve the cube.


## How It Works

1. **Face Detection**: The `face_detection.py` module uses OpenCV to capture images of each face of the Rubik's Cube. The user is prompted to rotate the cube to show all six faces to the webcam.

2. **Solving the Cube**: The captured face data is processed and fed into the `kociemba_solver.py` module, which uses the Kociemba algorithm to calculate the optimal solution.

3. **Output**: The solution is displayed as a sequence of moves, which the user can follow to solve the Rubik's Cube.



## Acknowledgements
- [OpenCV](https://opencv.org/) for the computer vision functionality.
- [Kociemba](https://github.com/hkociemba/RubiksCube-TwophaseSolver) for the Rubik's Cube solving algorithm.

---

## Additional Information

Only one of the 43 quintillion possible states of the original-size Rubik's cube (3x3x3) is the desired solved state. The challenge in solving the cube is to find an algorithm that solves the cube in the fewest steps possible. The Kociemba algorithm, which requires some pre-processing tasks like depth-first search and tree pruning, can solve the cube in fewer moves. 

As a result, we will be developing a program to solve a Rubik's cube using Python and OpenCV as a team. To accomplish this, we will extract all of the cubies' colours and then use Kociemba's algorithm to return a solution to the users. To do this, we will extract all of the cubies' colours and then apply HSV color scale to provide a solution to convert the BGR to HSV and detect the faces of the cube in each and every environment possible. 

The aim of a Rubik's Cube problem is to start with a randomised, scrambled, and jumbled cube configuration and, by rotating the faces, return it to the original solved pattern with each side being a single colour.
