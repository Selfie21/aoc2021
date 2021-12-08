import numpy as np
from numpy import int16

with open("inputs/8", "r") as file:
    lines = file.read().splitlines()
    lines = [line.split(' | ') for line in lines]


def add_chars_from_string_to_set(my_str, my_set):
    for char in my_str:
        my_set.add(char)


def contains_all(my_str, my_set):
    return 0 not in [c in my_str for c in my_set]

output = 0

for line in lines:
    unique_signals = np.array(line[0].split(' '))
    digit_outputs = np.array(line[1].split(' '))
    nums = ['' for i in range(10)]
    configs = [set() for i in range(7)]

    nums[1] = [signal for signal in unique_signals if len(signal) == 2][0]
    add_chars_from_string_to_set(nums[1], configs[2])
    add_chars_from_string_to_set(nums[1], configs[5])

    nums[7] = [signal for signal in unique_signals if len(signal) == 3][0]
    for char in nums[7]:
        if not(char in configs[2]):
            configs[0].add(char)

    nums[4] = [signal for signal in unique_signals if len(signal) == 4][0]
    for char in nums[4]:
        if not(char in configs[2]):
            configs[1].add(char)
            configs[3].add(char)

    nums[8] = [signal for signal in unique_signals if len(signal) == 7][0]
    for char in nums[8]:
        if not(char in configs[2]) and not(char in configs[1]) and not(char in configs[0]):
            configs[4].add(char)
            configs[6].add(char)

    nums[2] = ''
    for signal in unique_signals:
        tmp = list(configs[4])
        if len(signal) == 5 and (tmp[0] in signal) and (tmp[1] in signal):
            nums[2] = signal
            break

    three_and_five = list(filter(lambda i: not(i == nums[2]) and len(i) == 5, unique_signals))
    tmp = list(configs[4])
    if tmp[0] in three_and_five:
        configs[6].remove(tmp[1])
        configs[4].remove(tmp[0])
    else:
        configs[6].remove(tmp[0])
        configs[4].remove(tmp[1])

    for signal in three_and_five + [nums[2]]:
        tmp = list(configs[1])
        if (tmp[0] in signal) and (tmp[1] in signal):
            nums[5] = signal
            break

    nums[3] = list(filter(lambda i: not (i == nums[5]), three_and_five))[0]

    tmp = list(configs[1])
    if tmp[0] in nums[2]:
        configs[1].remove(tmp[0])
        configs[3].remove(tmp[1])
    else:
        configs[1].remove(tmp[1])
        configs[3].remove(tmp[0])

    tmp = configs[1].union(configs[3])
    nums[0] = [signal for signal in unique_signals if len(signal) == 6 and not(contains_all(signal, tmp))][0]

    tmp = configs[4].union(configs[6])
    nums[9] = [signal for signal in unique_signals if len(signal) == 6 and not (contains_all(signal, tmp))][0]
    nums[6] = list(set(unique_signals) - set(nums))[0]
    final_number_per_line = ''

    for output_num in digit_outputs:
        for i, num in enumerate(nums):
            if set(num) == set(output_num):
                final_number_per_line += str(i)
    output += int(final_number_per_line)

print(output)


