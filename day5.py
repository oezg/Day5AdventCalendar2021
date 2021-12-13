import numpy as np


def line_overlap(lines):
    lines = [line.rstrip().split(" -> ") for line in lines]
    lines = [[coord.split(',') for coord in line] for line in lines]
    lines = [[[int(num) for num in coord] for coord in line] for line in lines]
    lines = np.array(lines)
    field = np.zeros((lines.max()+1,lines.max()+1),np.int8)
    for line in lines:
        if line[0,0] == line[1,0]:
            if line[0,1] <= line[1,1]:
                field[line[0,1]:line[1,1]+1, line[0,0]] += 1
            else:
                field[line[1,1]:line[0,1]+1, line[0,0]] += 1
        elif line[0,1] == line[1,1]:
            if line[0,0] <= line[1,0]:
                field[line[0,1], line[0,0]:line[1,0]+1] += 1
            else:
                field[line[0,1], line[1,0]:line[0,0]+1] += 1
        elif abs(line[0,0] - line[1,0]) == abs(line[0,1] - line[1,1]):
            m = 1 if line[0,0] < line[1,0] else -1
            n = 1 if line[0,1] < line[1,1] else -1
            for i in range(abs(line[0,0] - line[1,0]) + 1):
                    field[line[0,1] + n * i, line[0,0] + m * i] += 1
    count = np.count_nonzero(field > 1)
    print(field)
    return count


with open("day5_input") as inp:
    lines = inp.readlines()
print(line_overlap(lines))
