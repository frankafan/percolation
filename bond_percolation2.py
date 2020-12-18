import numpy as np
import random
import matplotlib.pyplot as plt

P = 0.6
N = 100

lattice = np.zeros((N, N))
vertical_bonds = []
horizontal_bonds = []
for y in range(N):
    for x in range(N):
        if y < N - 1:
            vertical_bonds.append([[x, y], [x, y + 1]])
        if x < N - 1:
            horizontal_bonds.append([[x, y], [x + 1, y]])

for i in range(len(vertical_bonds)):
    if random.random() < P:
        vertical_bonds[i] = False
    if random.random() < P:
        horizontal_bonds[i] = False


for i in range(len(vertical_bonds)):
    if vertical_bonds[i]:
        vertical_bond_x = [vertical_bonds[i][0][0], vertical_bonds[i][1][0]]
        vertical_bond_y = [vertical_bonds[i][0][1], vertical_bonds[i][1][1]]
        plt.plot(vertical_bond_x, vertical_bond_y, 'black')
    if horizontal_bonds[i]:
        horizontal_bond_x = [horizontal_bonds[i][0][0], horizontal_bonds[i][1][0]]
        horizontal_bond_y = [horizontal_bonds[i][0][1], horizontal_bonds[i][1][1]]
        plt.plot(horizontal_bond_x, horizontal_bond_y, 'black')

plt.show()
