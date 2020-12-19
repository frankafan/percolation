import numpy as np
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

N = 100  # width and length of the network
P = 0.5  # probability of a given site to be open
SAVEFIG = True

bonds = []  # initialize array that stores coordinates of all the bonds
for y in range(N):  # iterate through the lattice
    for x in range(N):
        if y < N - 1:  # if the current site is not the bottom row
            bonds.append([[x, y], [x, y + 1]])  # the current site connects with
            # the site below it, and we store the coordinates of the two connected
            # sites in an array of two arrays, which we put into the overall bond
            # array
        if x < N - 1:  # if the current site is not the very right column
            bonds.append([[x, y], [x + 1, y]])  # the current site connects with
            # the site to the right of it, and we store the coordinates of the
            # two connected sites in an array of two arrays, which we put into
            # the overall bond array

for i in range(len(bonds)):  # iterate through every bond
    if random.random() < (1 - P):  # if the bond is stochastically not open
        bonds[i] = False  # change the bond to False

bond_flattened = []  # itialize an array that stores the coordinates of all the
# sites that have an open bond at that position
for bond in bonds:  # iterate through the coordinates of each particular bond
    if bond:  # if the term is not False, hence the bond exists
        bond_flattened.extend(bond)  # put the coordinate into the flattened array


# plot figure of bonds
plt.figure()
for i in range(len(bonds)):  # iterate through each bond
    if bonds[i]:  # if the term is not False, hence the bond exists
        bond_x = []  # initiate array for plotting
        bond_y = []
        for j in range(len(bonds[i])):  # iterate through each coordinate within
            # this particular bond
            bond_x.append(bonds[i][j][0])  # add the x coordinate to the x array
            bond_y.append(bonds[i][j][1])  # add the y coordinate to the y array
        plt.plot(bond_x, bond_y, 'black')
plt.ylim([N, 0])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Example of a 10 by 10 bond-percolating lattice")
if SAVEFIG:
    plt.savefig("4")

lattice = np.zeros((N, N))


def update_lattice(x_, y_):
    if x_ < 0 or x_ >= N:  # if the site is outside the boundary
        return None  # reject
    if y_ < 0 or y_ >= N:  # if the site is outside the boundary
        return None  # reject
    if lattice[y_][x_]:  # if the site is already marked as a full site
        return None  # reject
    if [x_, y_] not in bond_flattened:  # if the site does not have any bonds connected to it
        return None  # reject

    lattice[y_][x_] = 1  # mark current site as full

    for bond in bonds:  # iterate through bonds
        if bond and len(bond) > 1 and [x_, y_] in bond:  # if there are
            # coordinates of two sites and the current site has a connected bond
            del bond[(bond.index([x_, y_]))]  # delete the coordinate of the current site
            update_lattice(bond[0][0], bond[0][1])  # check the site that is
            # connected to the current site


for x in range(N):  # iterate through the top row of the lattice, where water enters
    update_lattice(x, 0)  # start checking

percolates = False  # the system does not percolate in its default state
for x in range(N):  # iterate through the bottom row of the lattice, where water resides after percolation
    if lattice[N - 1][x] == 1:  # if a site at this point of the bottom row is full
        percolates = True  # the system percolates
print(percolates)

# plot lattice of full sites
plt.figure()
plt.imshow(lattice, cmap='gray')
plt.xlabel("x")
plt.ylabel("y")
if SAVEFIG:
    plt.savefig("4_")

plt.show()
