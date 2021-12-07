import numpy as np
from numpy import int16

with open("inputs/7", "r") as file:
    line = file.readline()
    submarine_data = np.array(line.split(','), dtype=int16)

start = np.min(submarine_data)
end = np.max(submarine_data)
min_fuel = 999999999999999

for i in range(start, end + 1):
    lin_fuel_to_dest = np.absolute(submarine_data - i)
    squared_fuel_to_dest = np.array(list(map(lambda j: np.sum(np.arange(1, j+1)), lin_fuel_to_dest)))
    fuel_usage = np.sum(squared_fuel_to_dest)
    if min_fuel > fuel_usage:
        min_fuel = fuel_usage
print(min_fuel)
