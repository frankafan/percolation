import numpy as np
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

N = 50
trials = 1000
SAVEFIG = True


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


percolation_rates = []
j = 1
for P in np.arange(0.3, 0.7, 0.01):
    print(P)
    percolations = 0

    for n in range(trials):
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

        lattice = np.zeros((N, N))

        for x in range(N):
            update_lattice(x, 0)

        percolates = False
        for x in range(N):
            if lattice[N - 1][x] == 1:
                percolates = True
        # print(percolates)

        if percolates:
            percolations += 1

    percolation_rates.append(percolations / trials)

plt.figure()
plt.plot(np.arange(0.3, 0.7, 0.01), percolation_rates)
plt.xlabel("$p$")
plt.ylabel("Percolation probability")
plt.title(f"Percolation probability over $p$ for {trials} trials")
if SAVEFIG:
    plt.savefig(f"Percolation probability over p for {trials} trials.png")
plt.show()

plt.show()
