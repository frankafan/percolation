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

for i in range(len(bonds)):
    if bonds[i]:
        bond_x = []
        bond_y = []
        for j in range(len(bonds[i])):
            bond_x.append(bonds[i][j][0])
            bond_y.append(bonds[i][j][1])
        plt.plot(bond_x, bond_y, 'black')

plt.show()
