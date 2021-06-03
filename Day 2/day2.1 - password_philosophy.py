with open("day2.txt", 'r') as f:
    data = [i for i in f]

count = 0
valid_password = 0
for info in data:
    info = info.split()
    numbers = info[0].split("-")
    low_num = int(numbers[0])
    high_num = int(numbers[1])
    letter = info[1].strip(':')
    password = info[2]
    length = len(password)
    for i in range(len(password)):
        if password[i] == letter:
            count += 1
        if i == length - 1:
            if count >= low_num and count <= high_num:
                valid_password += 1
            count = 0

print(valid_password)
