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
print(open)

full[0] = open[0]
for y in range(N):
    for x in range(N):
        if full[y][x]:
            if x > 0 and open[y][x - 1]:
                full[y][x - 1] = 1
            if x < N - 1 and open[y][x + 1]:
                full[y][x + 1] = 1
            if y > 0 and open[y - 1][x]:
                full[y - 1][x] = 1
            if y < N - 1 and open[y + 1][x]:
                full[y + 1][x] = 1

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
