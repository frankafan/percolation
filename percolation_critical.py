import numpy as np
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

N = 50  # width and length of the network
trials = 10000
vertical = False
SAVEFIG = True


def update_full(x_, y_, vertical_):
    if x_ < 0 or x_ >= N:
        return None
    elif y_ < 0 or y_ >= N:
        return None
    elif not open[y_][x_]:
        return None
    elif full[y_][x_]:
        return None

    full[y_][x_] = 1

    update_full(x_ + 1, y_, vertical)
    update_full(x_ - 1, y_, vertical)
    update_full(x_, y_ + 1, vertical)
    if not vertical_:
        update_full(x_, y_ - 1, vertical)


percolation_rates = []
j = 1
for P in np.arange(0.1, 1, 0.01):
    percolations = 0
    for i in range(trials):
        open = np.zeros((N, N))
        full = np.zeros((N, N))
        for y in range(N):
            for x in range(N):
                if random.random() < P:
                    open[y][x] = 1

        for x in range(N):
            update_full(x, 0, vertical)

        percolates = False
        for x in range(N):
            if full[N - 1][x] == 1:
                percolates = True
        # print(percolates)

        if percolates:
            percolations += 1

    if not round(P, 2) * 10 % 1:
        plt.figure()
        plt.imshow(open, cmap='gray')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Lattice of open and closed sites at p = {round(P, 2)}")
        if SAVEFIG:
            plt.savefig(f"{j}")

        plt.figure()
        plt.imshow(full, cmap='gray')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(
            f"Lattice of full and empty / closed sites at p = {round(P, 2)}")
        if SAVEFIG:
            plt.savefig(f"{j}_")
        j += 1

    percolation_rates.append(percolations / trials)

print(percolation_rates)

plt.figure()
plt.plot(np.arange(0.1, 1, 0.01), percolation_rates)
plt.xlabel("$p$")
plt.ylabel("Percolation probability")
plt.title(f"Percolation probability over $p$ for {trials} trials")
if SAVEFIG:
    plt.savefig(f"Percolation probability over p for {trials} trials.png")
plt.show()
