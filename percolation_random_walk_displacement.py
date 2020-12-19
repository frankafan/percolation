import numpy as np
import random
import matplotlib.pyplot as plt

N = 100  # width and length of the network
P = 0.59  # probability of a given site to be open
particles = 100
steps = 10000

open = np.zeros((N, N))
full = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            open[y][x] = 1


def update_full(x_, y_, id_):
    if x_ < 0 or x_ >= N:
        return None
    if y_ < 0 or y_ >= N:
        return None
    if not open[y_][x_]:
        return None
    if full[y_][x_]:
        return None

    full[y_][x_] = id_

    update_full(x_ + 1, y_, id_)
    update_full(x_ - 1, y_, id_)
    update_full(x_, y_ + 1, id_)
    update_full(x_, y_ - 1, id_)


id = 0
for y in range(N):
    for x in range(N):
        if open[y][x] and not full[y][x]:
            id += 1
            update_full(x, y, id)


# print(full)
# print(max(np.ndarray.flatten(full)))


def next_move(x_, y_, full_):
    """ randomly choose a direction
    0 = up, 1 = down, 2 = left, 3 = right"""
    options = np.arange(4).tolist()  # array of the possible directions
    id_self = full_[y_][x_]
    # remove the illegal move depending on the particle's edge case
    if y_ == 0 or full_[y_ - 1][x_] != id_self:
        options.pop(options.index(0))
    if y_ == N - 1 or full_[y_ + 1][x_] != id_self:
        options.pop(options.index(1))
    if x_ == 0 or full_[y_][x_ - 1] != id_self:
        options.pop(options.index(2))
    if x_ == N - 1 or full_[y_][x_ + 1] != id_self:
        options.pop(options.index(3))
    if not options:
        return x_, y_
    direction = options[random.randint(0, len(options) - 1)]

    if direction == 0:  # move up
        y_ -= 1
    elif direction == 1:  # move down
        y_ += 1
    elif direction == 2:  # move left
        x_ -= 1
    elif direction == 3:  # move right
        x_ += 1
    else:
        print("error: direction isn't 0-3")

    return x_, y_


paths_x = []
paths_y = []
displacements = []
for i in range(particles):
    start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    while not open[start_y][start_x]:
        start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    path_x, path_y = [start_x], [start_y]
    displacement = []
    for j in range(steps):
        xp, yp = next_move(path_x[-1], path_y[-1], full)
        path_x.append(xp)
        path_y.append(yp)
        if j == 0:
            if xp == start_x and yp == start_y:
                break
        displacement.append(np.sqrt((start_x - xp) ** 2 + (start_y - yp) ** 2))
    displacements.append(displacement)
    paths_x.append(path_x)
    paths_y.append(path_y)

displacement_total = np.arange(0, steps, 1)
for i in range(particles):
    for j in range(steps):
        if len(displacements[i]):
            displacement_total[j] += displacements[i][j]

plt.figure()
plt.plot(np.arange(0, steps, 1), displacement_total)
plt.title(f"Total displacement of {particles} particles over {steps} steps")
plt.xlabel("Steps")
plt.ylabel("Displacement")
plt.show()
