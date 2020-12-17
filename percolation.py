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
print(open)


def update_full(x_, y_, open_, full_):
    if x_ < 0 or x_ >= N:
        return None
    elif y_ < 0 or y_ >= N:
        return None
    elif not open_[y_][x_]:
        return None
    elif full_[y_][x_]:
        return None

    full_[y_][x_] = 1

    update_full(x_ + 1, y_, open_, full_)
    update_full(x_ - 1, y_, open_, full_)
    update_full(x_, y_ + 1, open_, full_)
    update_full(x_, y_ - 1, open_, full_)


for x in range(N):
    update_full(x, 0, open, full)

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
