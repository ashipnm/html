n=3
for i in range(3):
    for j in range(i+1):
        print( end='')
    for k in range(2*i+1):
        print(chr(65 + k), end='')
    print()