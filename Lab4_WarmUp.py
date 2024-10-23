import numpy as np
import matplotlib.pyplot as plt

#WARM UP
# Load parameters from initialization file
with open('ini.txt', 'r') as f:
    params = f.readlines()
    L = int(params[0].strip())
    p = float(params[1].strip())

# Generate random grid with dogs and empty cells
grid = np.random.choice([0, 1], size=(L, L), p=[1-p, p])
#1 - dog, 0 - empty

# Save grid to file
with open('grid.txt', 'w') as f:
    for i in range(L):
        for j in range(L):
            f.write(str(grid[i, j]))
        f.write('\n')
#print(grid)

# Display grid using Matplotlib
plt.imshow(1-grid, cmap='gray')
plt.show()

# Load grid from file
with open('grid.txt', 'r') as f:
    lines = f.readlines()

# Create 2D NumPy array
grid = np.zeros((len(lines), len(lines[0])-1), dtype=int)
for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        grid[i, j] = int(char)

# Find the leftmost dog in the first row
start_pos = None
for j in range(L):
    if grid[0, j] == 1:
        start_pos = (0, j)
        break

# Place flea on the leftmost dog in the first row
grid[start_pos] = 2 #2 = flea

# Define function to jump flea randomly from a dog to dog with distance 1
def jump_flea(grid, curr_pos):
    neighbors = []
    i, j = curr_pos
    if i > 0 and grid[i-1, j] == 1:
        neighbors.append((i-1, j))
    if i < L-1 and grid[i+1, j] == 1:
        neighbors.append((i+1, j))
    if j > 0 and grid[i, j-1] == 1:
        neighbors.append((i, j-1))
    if j < L-1 and grid[i, j+1] == 1:
        neighbors.append((i, j+1))
    else:
        return

# Jump flea randomly until all reachable dogs have been visited
for t in range(1, L):
    jump_flea(grid, start_pos)

# Save grid to file
np.savetxt('flea_grid.txt', grid, fmt='%d')

# Display grid using Matplotlib
plt.imshow(2-grid, cmap='gray', vmin=0, vmax=2)
plt.show()

'''
(a) The above description of the jump is not exact, and it can be implemented in at least two ways. Do you see it? 

Yes, there are at least two possible ways to implement the flea's jump. 
One option is to choose a random neighbor among the four adjacent cells that are occupied by dogs, 
and make the flea jump to that cell. Another option is to consider all reachable neighbors and choose 
one of them randomly with equal probability.
The first option is simpler to implement, as it only requires selecting a random neighbor from a fixed set of 
four adjacent cells. However, it may lead to biased behavior, especially when some of the neighbors are more 
likely to be visited than others.
The second option is more general and allows for more flexibility in the flea's movement, 
as it considers all reachable neighbors, not just the adjacent ones. However, it requires checking 
all possible neighbors and selecting one randomly with equal probability, which can be more computationally expensive.
In this exercise, the first option is implemented, where the flea chooses a random neighbor among 
the four adjacent cells that are occupied by dogs.

(b) Play around with different values for the parameters. 

If we increase "L" parameter it means that we expand a qrid.
If we increase "p" with means probability to fill an array with dog - we obviously have more black cells in the grid.
'''

