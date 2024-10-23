# Warm-Up and Site Percolation Simulations

This project implements two main simulations: a **grid-based flea hopping model** and a **site percolation problem** on a square lattice. The first part simulates a random walk of a flea on a grid of dogs, and the second part uses Monte Carlo simulations to solve the site percolation problem, analyzing the probability of a path forming across the lattice.

## Project Structure


## 1. Warm-Up: Flea Hopping on a Grid

### Description

- A grid `L x L` is generated, where each cell can either contain a dog (`1`) or be empty (`0`) based on a probability `p`.
- The flea starts on the leftmost dog in the first row and jumps randomly to neighboring dogs. Each visited dog is marked as `2`, and the flea's path is tracked.
- The parameters `L`, `p`, and time `t` are loaded from an initialization file `ini.txt`, which allows flexible user control.

### Tasks

1. **Grid Setup**: The grid is filled with dogs (`1`) or left empty (`0`) based on probability `p`. This configuration is saved to a file and visualized.
2. **Flea Movement**: The flea starts from the first dog and moves randomly across the grid. The visited sites are saved and visualized at the end of the simulation.
3. **Exploration**: Different movement strategies can be implemented for the flea's jumping behavior.


## 2. Site Percolation Problem

### Description

The site percolation problem involves a square lattice where each site is independently occupied with a probability `p`. The goal is to determine the probability `Pflow` that a path exists from the first row to the last row using Monte Carlo simulations.

### Tasks

1. **Site Occupation**: For each site in the `L x L` grid, assign a value `1` (occupied) or `0` (empty) based on probability `p`.
2. **Path Check**: Use the **Burning Algorithm** to check if a path exists connecting the first and last row.
3. **Monte Carlo Simulation**: Run multiple trials (`T` trials) to estimate the probability `Pflow` as a function of `p`. The result is stored in a file following the format: `Ave-L{L}T{T}.txt`.
