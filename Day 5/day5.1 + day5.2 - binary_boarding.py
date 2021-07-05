from math import ceil

with open("day5.txt") as f:
    file = f.readlines()
results = []


def binary_boarding_check(seat, results):
    row = 0
    row_start = 0
    row_end = 127
    col = 0
    col_start = 0
    col_end = 7

    step = 0

    while step <= len(seat) - 1:
        if seat[step] == "F":
            row_end = (row_start + row_end) / 2
        if seat[step] == "B":
            row_start = (row_start + row_end) / 2
        if seat[step] == "L":
            col_end = (col_start + col_end) / 2
        if seat[step] == "R":
            col_start = (col_start + col_end) / 2

        row = row_start
        col = col_start
        step += 1
    results.append((ceil(row) * 8) + ceil(col))


for boarding_pass in file:
    binary_boarding_check(boarding_pass, results)
print(max(results))

for e, i in enumerate(sorted(results), min(results)):
    if e == i:
        continue
    else:
        print(e)
        break
