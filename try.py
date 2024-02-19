size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("■", end="  ")
        else:
            print("□", end="  ")
    print()
