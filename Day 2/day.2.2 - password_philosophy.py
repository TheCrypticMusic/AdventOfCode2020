with open("day2.txt", 'r') as f:
    data = [i.replace("-", " ").replace(":", " ").replace("\n", "") for i in f]

# Refactored
count = 0
for i in data:
    low, high = int(i.split()[0]), int(i.split()[1])
    letter = i.split()[2]
    password = i.split()[3]

    for index, elem in enumerate(password, 1):
        if index == low:
            if password[high - 1] == letter and password[low - 1] != letter:
                count += 1
            if password[high - 1] != letter and password[low - 1] == letter:
                count += 1
print(count)

# First Attempt
# count = 0
# good_passwords = 0
# for info in data:
#     info = info.split()
#     numbers = info[0].split("-")
#     low_num = int(numbers[0])
#     high_num = int(numbers[1])
#     letter = info[1].strip(':')
#     password = info[2]
#     length = len(password)
#     for index, j in enumerate(password, 1):
#         if index == low_num:
#             if j == letter:
#                 count += 1
#         elif index == high_num:
#             if j == letter:
#                 count += 1
#         if index == length:
#             if count == 1:
#                 good_passwords += 1
#                 count = 0
#             else:
#                 count = 0
