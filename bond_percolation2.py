import numpy as np
import random
import matplotlib.pyplot as plt

P = 0.6
N = 10

lattice = np.zeros((N, N))
bonds = []
for y in range(N):
    for x in range(N):
        if y < N - 1:
            bonds.append([[x, y], [x, y + 1]])
        if x < N - 1:
            bonds.append([[x, y], [x + 1, y]])

for i in range(len(bonds)):
    if random.random() < P:
        bonds[i] = False


def connect_bonds(self, neighbor):
    if not self or not neighbor:
        return
    if self == neighbor:
        return

    if self[0] == neighbor[-1]:
        self = neighbor[0:len(neighbor) - 1] + self
        neighbor = False
    elif self[-1] == neighbor[0]:
        self = self + neighbor[1:len(neighbor)]
        neighbor = False
    return self, neighbor


for i in range(len(bonds)):
    for j in range(len(bonds)):
        connect_bonds(bonds[i], bonds[j])
print(bonds)

for i in range(len(bonds)):
    if bonds[i]:
        bond_x = []
        bond_y = []
        for j in range(len(bonds[i])):
            bond_x.append(bonds[i][j][0])
            bond_y.append(bonds[i][j][1])
        plt.plot(bond_x, bond_y)

plt.show()
