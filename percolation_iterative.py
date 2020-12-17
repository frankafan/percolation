import numpy as np
import random
import matplotlib.pyplot as plt

N = 10  # width and length of the network
P = 0.5  # probability of a given site to be open

open = np.zeros((N, N))
full = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            open[y][x] = 1


def get_neighbors(x_, y_):
    neighbors = []
    if x > 0:
        neighbors.append([x_ - 1, y_])
    if y > 0:
        neighbors.append([x_, y_ - 1])
    if x < N - 1:
        neighbors.append([x_ + 1, y_])
    if y < N - 1:
        neighbors.append([x_, y_ + 1])
    return neighbors


clusters = []
for y in range(N):
    for x in range(N):
        print(x, y)
        if open[y][x]:
            cluster = []
            cluster_candidates = [[x, y]]
            while len(cluster_candidates):
                print(len(cluster_candidates))
                top = cluster_candidates[0]
                if not full[top[0], top[1]] and open[top[0], top[1]]:
                    full[top[1]][top[0]] = 1
                    cluster.append(top)
                    cluster_candidates.extend(get_neighbors(x, y))
                cluster_candidates.pop(0)
            if len(cluster):
                clusters.append(cluster)

print(clusters)
for cluster_id in range(len(clusters)):
    for coordinates in clusters[cluster_id]:
        full[coordinates[1], coordinates[0]] = cluster_id + 1

percolates = False
for x in range(N):
    if full[N - 1][x] == 1:
        percolates = True
print(percolates)

plt.figure()
plt.imshow(open, cmap="gray")

plt.figure()
plt.imshow(full)
print(full)
plt.show()
