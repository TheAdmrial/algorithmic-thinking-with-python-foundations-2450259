# making the doors
doors = [False]*101

# print(doors)

# for i in range(1,101):
#     doors[i] = not doors[i]

# print(doors)

# for i in range(1,6):
#     for j in range(1,4):
#         print('i:', i, "j:", j)

# for i in range(1,11, 2):
#     print(i)

for i in range(1, 101):
    for j in range(1,101,i):
        doors = not doors[j]

### SOLUTION ###

for i in range(1, 101):
    for j in range(1,101,i):
        doors[j] = not doors[j]

for i in range(1,101):
    if doors[i] is True:
        print(i, end = ', ')