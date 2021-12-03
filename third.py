file = open("inputs/3", "r")
lines = file.read().splitlines()
lines = [str(line) for line in lines]

#gamma rate most common 0,1
#epsilon least common 0,1

zeros = 0
ones = 0
gamma = ''
epsilon = ''
for i in range(len(lines[0])):
    for line in lines:
        if line[i] == '0':
            zeros += 1
        elif line[i] == '1':
            ones += 1
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    zeros = 0
    ones = 0


def dnc(data, common=True, idx=0):
    if len(data) == 1:
        return data[0]

    divided_data = {1: [], 0: []}
    for d in data:
        if int(d[idx]):
            divided_data[1].append(d)
        else:
            divided_data[0].append(d)
    if len(divided_data[0]) == len(divided_data[1]) and common:
        return dnc(divided_data[1], common, idx+1)
    elif len(divided_data[0]) == len(divided_data[1]) and not common:
        return dnc(divided_data[0], common, idx+1)
    elif (len(divided_data[0]) > len(divided_data[1])) ^ common:
        return dnc(divided_data[1], common, idx+1)
    else:
        return dnc(divided_data[0], common, idx+1)


print(int(gamma, 2) * int(epsilon, 2))

oxygen_rate, scrubber_rate = dnc(lines), dnc(lines, False)
print(int(oxygen_rate, 2) * int(scrubber_rate, 2))


