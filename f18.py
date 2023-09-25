for i in range(3):
    decr=0
    count = 0
    for k in range(decr):
        print(end=" ")
    decr = decr - 2
    for j in range(i):
        count = count + 1
    num = count+65
    ch = chr(num)
    for j in range(i+1):
        print(ch, end=" ")
        num = num - 1
        ch = chr(num)
    print()