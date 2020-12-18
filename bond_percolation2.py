import numpy as np
import random
import matplotlib.pyplot as plt

P = 0.6
N = 3

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

print(vertical_bonds)
