# tic tac toe
import sys
import os

def element(m, x, y):
    return m[10 * x + y]

def verify_direction(m, start_x, start_y, increment_x, increment_y):
    c = element(m, start_x, start_y)
    for i in range(0, 4):
        start_x += increment_x
        start_y += increment_y
        if start_y < 0 or start_x < 0 or start_x >= 10 or start_y >= 10:
            return False
        testc = element(m, start_x, start_y)
        if testc != c:
            return False
    return True
   

if len(sys.argv) != 2:
    print("you must specify a filename")
    exit()

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"the file {filename} does not exist")

matrix = []
with open(filename) as f:
    linenumber = 0
    for line in f:
        linenumber += 1
        line = line.strip()
        print(line)
        if len(line) != 10:
            print(f"invalid line at line {linenumber} - length is {len(line)}")
            exit()
        for c in line:
            matrix.append(c)

for i in range(0, 10):
    for j in range(0, 10):
        print(f"{element(matrix, i, j)}", end=" ")
    print()

for i in range(0, 10):
    for j in range(0, 10):
        currentElement = element(matrix, i, j)
        if currentElement != '.':
            for x_increment in [-1, 0, 1]:
                for y_increment in [-1, 0, 1]:
                    if (x_increment != 0 or y_increment != 0) and verify_direction(matrix, i, j, x_increment, y_increment):
                        print(f"{i} {j} {x_increment} {y_increment}")


        




