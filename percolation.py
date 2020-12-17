import numpy as np
import random
import matplotlib.pyplot as plt

N = 10  # width and length of the network
P = 0.5  # probability of a given site to be open

network = np.zeros((N, N))
for y in range(N):
    for x in range(N):
        if random.random() < P:
            network[y][x] = 1
print(network)
