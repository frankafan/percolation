import numpy as np
import random
import matplotlib.pyplot as plt

N = 10  # width and length of the network
P = 0.6  # probability of a given site to be open

open = np.zeros((N, N))
full = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            open[y][x] = 1
# print(open)


def update_full(x_, y_, id_):
    if x_ < 0 or x_ >= N:
        return None
    if y_ < 0 or y_ >= N:
        return None
    if not open[y_][x_]:
        return None
    if full[y_][x_]:
        return None

    full[y_][x_] = id_

    update_full(x_ + 1, y_, id_)
    update_full(x_ - 1, y_, id_)
    update_full(x_, y_ + 1, id_)
    update_full(x_, y_ - 1, id_)


id = 0
for y in range(N):
    for x in range(N):
        if not full[y][x]:
            id += 1
            update_full(x, y, id)
print(full)


percolates = False
for x in range(N):
    if not full[N - 1][x]:
        percolates = True
print(percolates)

plt.figure()
plt.imshow(open, cmap='gray')

plt.figure()
plt.imshow(full)

plt.show()
