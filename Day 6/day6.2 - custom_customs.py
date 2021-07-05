with open("day6") as f:
    file = f.read().split("\n\n")

new_file = [x.replace("\n", " ").split() for x in file]

count = 0
d = {}

for i in new_file:
    for j in i:
        word = "".join(i)
        test = len(i)
        if len(i) == 1:
            count += len(j)
        else:
            for h in j:
                if h in d:
                    d[h] += 1
                else:
                    d[h] = 1
    for key, value in d.items():
        if value == len(i):
            count += 1
    d = {}
print(count)
