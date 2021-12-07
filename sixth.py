import numpy as np
from numpy import int64

with open("inputs/6", "r") as file:
    line = file.readline()
    fish_data = np.array(line.split(','), dtype=int64)

    all_fish = np.zeros(9, dtype=int64)
    for i in range(9):
        all_fish[i] = np.sum(fish_data == i)

for i in range(256):
    new_fish = all_fish[0]
    all_fish[7] += new_fish
    all_fish[0] = 0
    for j in range(8):
        all_fish[j] = all_fish[j + 1]
    all_fish[8] = new_fish

print(sum(all_fish))


