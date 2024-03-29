import numpy as np
import random
import matplotlib.pyplot as plt

N = 100  # width and length of the network
P = 0.59  # probability of a given site to be open
particles = 10  # number of particles to random walk
steps = 2000  # numbr of steps for each particle to walk

open = np.zeros((N, N))  # same as percolation.py
full = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            open[y][x] = 1


def update_full(x_, y_, id_):  # same as percolation.py
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


id = 0  # same as percolation.py
for y in range(N):
    for x in range(N):
        if open[y][x] and not full[y][x]:
            id += 1
            update_full(x, y, id)





def next_move(x_, y_, full_):
    """ randomly choose a direction
    0 = up, 1 = down, 2 = left, 3 = right"""
    options = np.arange(4).tolist()  # array of the possible directions
    id_self = full_[y_][x_]
    # remove the illegal move depending on the particle's edge case
    if y_ == 0 or full_[y_ - 1][x_] != id_self:  # if current site is top row or the site above it is not at the same cluster
        options.pop(options.index(0))  # reject option
    if y_ == N - 1 or full_[y_ + 1][x_] != id_self:  # if current site is bottom row or the site below it is not at the same cluster
        options.pop(options.index(1))  # reject option
    if x_ == 0 or full_[y_][x_ - 1] != id_self:  # if current site is left column or the site left of it is not at the same cluster
        options.pop(options.index(2))  # reject option
    if x_ == N - 1 or full_[y_][x_ + 1] != id_self:  # if current site is right column or the site right of it is not at the same cluster
        options.pop(options.index(3))  # reject option
    if not options:
        return x_, y_
    direction = options[random.randint(0, len(options) - 1)]  # choose random option

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


paths_x = []  # initialize path arrays for plotting
paths_y = []
for i in range(particles):  # for each particle
    start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)  # start at a random site
    while not open[start_y][start_x]:  # while the site is closed, try again find a new random site
        start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    path_x, path_y = [start_x], [start_y]  # initialize array
    for j in range(steps):  # for each step
        xp, yp = next_move(path_x[-1], path_y[-1], full)  # make random move
        path_x.append(xp)  # add position to path array
        path_y.append(yp)
    paths_x.append(path_x)
    paths_y.append(path_y)

# print(paths_x, paths_y)

# plt.figure()
# plt.imshow(open, cmap='gray')
#
# plt.figure()
# plt.imshow(full)

plt.figure()
plt.imshow(full)
for i in range(len(paths_x)):
    plt.plot(paths_x[i], paths_y[i], label=i+1)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Paths of {particles} random-walking particles for {steps} steps")
plt.show()
