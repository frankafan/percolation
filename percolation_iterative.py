import numpy as np
import random
import matplotlib.pyplot as plt

N = 1000  # width and length of the network
P = 0.7  # probability of a given site to be open

open = np.zeros((N, N))
full = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            open[y][x] = 1

cluster_id = 1
clusters = []
cluster = []
for y in range(N):
    for x in range(N):
        if open[y][x] and not full[y][x]:
            cluster.append([x, y])
            has_neighbor = False
            if x > 0 and open[y][x - 1] and not full[y][x - 1]:
                cluster.append([x - 1, y])
                has_neighbor = True
            if x < N - 1 and open[y][x + 1] and not full[y][x + 1]:
                cluster.append([x + 1, y])
                has_neighbor = True
            if y > 0 and open[y - 1][x] and not full[y - 1][x]:
                cluster.append([x, y - 1])
                has_neighbor = True
            if y < N - 1 and open[y + 1][x] and not full[y + 1][x]:
                cluster.append([x, y + 1])
                has_neighbor = True
            if not has_neighbor:
                clusters.append(cluster)
                cluster = []

print(clusters)

percolates = False
for x in range(N):
    if full[N - 1][x] == 1:
        percolates = True
print(percolates)

plt.figure()
plt.imshow(open, cmap="gray")

plt.figure()
plt.imshow(full, cmap="gray")

plt.show()
