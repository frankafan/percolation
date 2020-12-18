import numpy as np
import random
import matplotlib.pyplot as plt

P = 0.50
N = 50

bonds = []
for y in range(N):
    for x in range(N):
        if y < N - 1:
            bonds.append([[x, y], [x, y + 1]])
        if x < N - 1:
            bonds.append([[x, y], [x + 1, y]])

for i in range(len(bonds)):
    if random.random() < (1 - P):
        bonds[i] = False
# print(bonds)

bond_flattened = []
for bond in bonds:
    if bond:
        bond_flattened.extend(bond)
# print(bond_flattened)

plt.figure()
for i in range(len(bonds)):
    if bonds[i]:
        bond_x = []
        bond_y = []
        for j in range(len(bonds[i])):
            bond_x.append(bonds[i][j][0])
            bond_y.append(bonds[i][j][1])
        plt.plot(bond_x, bond_y, 'black')
plt.ylim([N, 0])
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Lattice of connected bonds at p = {round(P, 2)}")

lattice = np.zeros((N, N))


def update_lattice(x_, y_):
    if x_ < 0 or x_ >= N:
        return None
    if y_ < 0 or y_ >= N:
        return None
    if lattice[y_][x_]:
        return None
    if [x_, y_] not in bond_flattened:
        return None

    lattice[y_][x_] = 1

    for bond in bonds:
        if bond and len(bond) > 1 and [x_, y_] in bond:
            del bond[(bond.index([x_, y_]))]
            update_lattice(bond[0][0], bond[0][1])


for x in range(N):
    update_lattice(x, 0)

percolates = False
for x in range(N):
    if lattice[N - 1][x] == 1:
        percolates = True
print(percolates)

plt.figure()
plt.imshow(lattice, cmap='gray')
plt.xlabel("x")
plt.ylabel("y")
plt.title(
    f"Lattice of spaces connected to the top edge by bonds at p = {round(P, 2)}")

plt.show()
