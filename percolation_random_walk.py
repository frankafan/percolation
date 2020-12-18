import numpy as np
import random
import matplotlib.pyplot as plt

N = 50  # width and length of the network
P = 0.6  # probability of a given site to be open
particles = 5
steps = 500

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
for i in range(particles):
    start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    while not open[start_y][start_x]:
        start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    path_x, path_y = [start_x], [start_y]
    for j in range(steps):
        xp, yp = next_move(path_x[-1], path_y[-1], full)
        path_x.append(xp)
        path_y.append(yp)
    paths_x.append(path_x)
    paths_y.append(path_y)

print(paths_x, paths_y)

# plt.figure()
# plt.imshow(open, cmap='gray')
#
# plt.figure()
# plt.imshow(full)

plt.figure()
for i in range(len(paths_x)):
    plt.plot(paths_x[i], paths_y[i])

plt.show()
