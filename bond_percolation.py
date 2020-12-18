import numpy as np
import random
import matplotlib.pyplot as plt

P = 0.5
N = 10

lattice = []
for y in range(N):
    row = []
    for x in range(N):
        row.append([])
    lattice.append(row)

for y in range(N):
    for x in range(N):
        for i in range(2):
            if random.random() < P:
                lattice[y][x].append(i)
# print(lattice)
full = np.zeros((N, N))


def update_full(x_, y_, id_):
    directions = lattice[y_][x_]
    if x_ < 0 or x_ >= N:
        return None
    if y_ < 0 or y_ >= N:
        return None

    full[y_][x_] = id_

    if 0 in directions and x_ < N - 1:
        update_full(x_ + 1, y_, id_)
    if 1 in directions and y_ < N - 1:
        update_full(x_, y_ + 1, id_)


id = 0
for y in range(N):
    for x in range(N):
        if not full[y][x]:
            id += 1
            update_full(x, y, id)

print(full)
