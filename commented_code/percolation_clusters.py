import numpy as np
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

N = 100  # width and length of the network
P = 0.7  # probability of a given site to be open
SAVEFIG = True

open = np.zeros((N, N))  # initialize lattice for open sites
full = np.zeros((N, N))  # initialize lattice for full sites
for y in range(N):
    for x in range(N):  # iterate through lattice
        if random.random() < P:  # if statement is true with probability of P
            open[y][x] = 1  # lattice at this site is open


def update_full(x_, y_, id_):
    if x_ < 0 or x_ >= N:  # if the site is outside the boundary
        return None  # reject
    elif y_ < 0 or y_ >= N:  # if the site is outside the boundary
        return None  # reject
    elif not open[y_][x_]:  # if the site is not open
        return None  # reject
    elif full[y_][x_]:  # if the site is already marked as a full site
        return None  # reject

    full[y_][x_] = id_  # mark current site with specified ID

    # check neighbors and give them the same ID if they are connected
    update_full(x_ + 1, y_, id_)
    update_full(x_ - 1, y_, id_)
    update_full(x_, y_ + 1, id_)
    update_full(x_, y_ - 1, id_)


id = 0  # initialize ID
for y in range(N):  # iterate through lattice
    for x in range(N):
        if open[y][x] and not full[y][x]:  # if the site is open and is not yet marked with ID
            id += 1
            update_full(x, y, id)  # update site with ID
print(full)
print(max(np.ndarray.flatten(full)))


# plot lattices
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
