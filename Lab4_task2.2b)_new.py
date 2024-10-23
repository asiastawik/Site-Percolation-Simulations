import numpy as np
import copy
import matplotlib.pyplot as plt
import time

with open('perc_ini.txt', 'r') as f:
    params = f.readlines()
    p_0 = float(params[0].strip())
    p_k = float(params[1].strip())
    d_p = float(params[2].strip())
    L = int(params[3].strip())
    T = int(params[4].strip())
    
T=100
p_k=1
d_p = 0.01
L_list = [10, 50, 100]
time_sum = []

def percolation_simulation(A, p, L):
   
    trial_A = np.copy(A)
    
    for i in range(L):
        for j in range(L):
            r = np.random.uniform()
            if r < p:
                trial_A[i][j] = 1
            else:
                trial_A[i][j] = 0
    t = 2

    # Initialize the top row with occupied sites marked as 2
    trial_A[0, :] *= 2

    while True:
        already_burned = []
        for i in range(L):
            for j in range(L):
                if trial_A[i][j] == t:
                    if i > 0 and trial_A[i - 1, j] == 1:
                        trial_A[i - 1][j] = t + 1
                        already_burned.append([(i - 1), j])
                    if i < L - 1 and trial_A[i + 1, j] == 1:
                        trial_A[i + 1][j] = t + 1
                        already_burned.append([(i + 1), j])
                    if j > 0 and trial_A[i, j - 1] == 1:
                        trial_A[i][j - 1] = t + 1
                        already_burned.append([i, (j - 1)])
                    if j < L - 1 and trial_A[i, j + 1] == 1:
                        trial_A[i][j + 1] = t + 1
                        already_burned.append([i, (j + 1)])
        if len(already_burned) == 0:
            return 0
        for j in range(L):
            if trial_A[-1][j] == t + 1:
                path = t - 1
                return path
        t += 1


# Store output data in file
for i, L, in enumerate(L_list):
    start1 = time.time()
    Pflow_list = []
    A = np.zeros((L, L))
    file = "Ave_L" + str(L) + "T" + str(T) + ".txt"
    with open(str(file), 'w') as f:
        f.write('p_0, p_k, d_p, L, T, Pflow\n')
        for p in np.arange(p_0, p_k + d_p, d_p):
            count = 0
            for t in range(T):
                is_zero = percolation_simulation(A, p, L)
                if is_zero > 0:
                    count += 1
            Pflow = count / T
            Pflow_list.append(Pflow)
            f.write('{},{},{},{},{},{}\n'.format(p_0, p_k, d_p, L, T, Pflow))
    markers = ['o', 's', 'd']
    sizes = [7, 4, 2]
    colors = ['0.8', '0.5', '0.2']
    legend_labels = ['L=10', 'L=50', 'L=100']
    i = L // 50 # reset i to 0, 1, or 2 depending on L
    plt.plot(np.arange(p_0, p_k + d_p, d_p), Pflow_list, linestyle='None', marker=markers[i % len(markers)], label=legend_labels[i % len(legend_labels)], markersize=sizes[i % len(sizes)], color=colors[i % len(colors)])
    end1 = time.time()
    time_count = end1 - start1
    print(time_count)
    time_sum.append(time_count)


# Plot results
plt.xlabel('p')
plt.ylabel('Pflow')
plt.title('Site Percolation on Square Lattice')
plt.legend()

print("Time taken by creating all output files: {:.6f} seconds".format(sum(time_sum)))