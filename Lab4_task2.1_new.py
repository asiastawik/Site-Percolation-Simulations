import numpy as np
import copy
import matplotlib.pyplot as plt

with open('perc_ini.txt', 'r') as f:
    params = f.readlines()
    p_0 = float(params[0].strip())
    p_k = float(params[1].strip())
    d_p = float(params[2].strip())
    L = int(params[3].strip())
    T = int(params[4].strip())
    
p_k2 = 0.6
p_k3 = 0.8
# p_0 = 0.1
# p_k = 0.9
# d_p = 0.1
p_range = [p_0, p_k, d_p] # range of p values
p_range2 = [p_0, p_k2, d_p] # range of p values
p_range3 = [p_0, p_k3, d_p] # range of p values
# L = 100 # size of lattice
# T = 100 # number of Monte Carlo simulations per p value

A = np.zeros((L, L))

def percolation_simulation(A, p):
   
    for i in range(L):
        for j in range(L):
            r = np.random.uniform()
            if r < p:
                A[i][j] = 1
            else:
                A[i][j] = 0
    t = 2

    # Initialize the top row with occupied sites marked as 2
    A[0, :] *= 2

    while True:
        already_burned = []
        for i in range(L):
            for j in range(L):
                if A[i][j] == t:
                    if i > 0 and A[i - 1, j] == 1:
                        A[i - 1][j] = t + 1
                        already_burned.append([(i - 1), j])
                    if i < L - 1 and A[i + 1, j] == 1:
                        A[i + 1][j] = t + 1
                        already_burned.append([(i + 1), j])
                    if j > 0 and A[i, j - 1] == 1:
                        A[i][j - 1] = t + 1
                        already_burned.append([i, (j - 1)])
                    if j < L - 1 and A[i, j + 1] == 1:
                        A[i][j + 1] = t + 1
                        already_burned.append([i, (j + 1)])
        if len(already_burned) == 0:
            return 0
        for j in range(L):
            if A[-1][j] == t + 1:
                path = t - 1
                return path
        t += 1


# Store output data in file
Pflow_list = []
file = "Ave_L" + str(L) + "T" + str(T) + ".txt"
with open(str(file), 'w') as f:
    f.write('p_0, p_k, d_p, L, T, Pflow\n')
    for p in np.arange(p_range3[0], p_range3[1] + p_range3[2], p_range3[2]):
        count = 0
        for t in range(T):
            trial_A = copy.copy(A)
            is_zero = percolation_simulation(trial_A, p)
            if is_zero > 0:
                count += 1
        Pflow = count / T
        Pflow_list.append(Pflow)
        f.write('{},{},{},{},{},{}\n'.format(p_0, p_k, d_p, L, T, Pflow))


# Plot results
plt.plot(np.arange(p_range3[0], p_range3[1] + p_range3[2], p_range3[2]), Pflow_list, 'o-', color='black', linestyle='None')
plt.xlabel('p')
plt.ylabel('Pflow')
plt.title('Site Percolation on Square Lattice')
plt.show()