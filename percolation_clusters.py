import numpy as np
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

N = 100  # width and length of the network
P = 0.7  # probability of a given site to be open
SAVEFIG = True

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
        if open[y][x] and not full[y][x]:
            id += 1
            update_full(x, y, id)
print(full)
print(max(np.ndarray.flatten(full)))

plt.figure()
plt.imshow(open, cmap='gray')
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Lattice of open and closed sites at p = {round(P, 2)}")
if SAVEFIG:
    plt.savefig("5")

plt.figure()
plt.imshow(full, cmap='gist_ncar')
plt.xlabel("x")
plt.ylabel("y")
plt.title(
    f"Lattice of full and empty / closed sites at p = {round(P, 2)}")
if SAVEFIG:
    plt.savefig("5_")

plt.show()
