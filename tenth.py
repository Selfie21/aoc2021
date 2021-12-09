import numpy as np
import itertools

# without \n
with open("inputs/9", "r") as file:
    lines = file.read().splitlines()
    height_map = np.array([[int(char) for char in line] for line in lines])

# with \n
with open("inputs/10", "r") as file:
    lines = file.readlines()

print("")