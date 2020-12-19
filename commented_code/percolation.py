import numpy as np
import random
import matplotlib.pyplot as plt

N = 100  # width and length of the network
P = 0.5  # probability of a given site to be open
vertical = False  # whether water can only go downwards in the lattice, False if water can go to connected open sites above itself

open = np.zeros((N, N))  # initialize lattice for open sites
full = np.zeros((N, N))  # initialize lattice for full sites
for y in range(N):
    for x in range(N):  # iterate through lattice
        if random.random() < P:  # if statement is true with probability of P
            open[y][x] = 1  # lattice at this site is open
print(open)


def update_full(x_, y_, vertical_):
    """Function that conditionally updates its own site as full and recursively
    enters its neighboring sites to check for the same thing"""
    if x_ < 0 or x_ >= N:  # if the site is outside the boundary
        return None  # reject
    elif y_ < 0 or y_ >= N:  # if the site is outside the boundary
        return None  # reject
    elif not open[y_][x_]:  # if the site is not open
        return None  # reject
    elif full[y_][x_]:  # if the site is already marked as a full site
        return None  # reject

    full[y_][x_] = 1  # mark current site as full

    # check all neighboring sites
    update_full(x_ + 1, y_, vertical)
    update_full(x_ - 1, y_, vertical)
    update_full(x_, y_ + 1, vertical)
    if not vertical_:
        update_full(x_, y_ - 1, vertical)


for x in range(N):  # iterate through the top row of the lattice, where water enters
    update_full(x, 0, vertical)  # start checking

percolates = False  # the system does not percolate in its default state
for x in range(N):  # iterate through the bottom row of the lattice, where water resides after percolation
    if full[N - 1][x] == 1:  # if a site at this point of the bottom row is full
        percolates = True  # the system percolates
print(percolates)

# plot lattices
plt.figure()
plt.imshow(open, cmap="gray")
plt.title(f"Lattice of open and closed sites at p = {round(P, 2)}")

plt.figure()
plt.imshow(full, cmap="gray")
plt.title(f"Lattice of full and empty / closed sites at p = {round(P, 2)}")
plt.show()
