space = 6
for i in range(4):
    for j in range(space):
        print(" ", end="")
    space = space-2
    for j in range(i+1):
        print("* ", end="")
    print()
