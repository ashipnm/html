#write a python program to find and print the pairs of numbers whose sum is equal to 18
x=[3,8,12,7,6,10,21,15]
sum=18
def sumlist(x,sum,len):
    print("Array=",x)
    print("Pairs whose sum is equal to  : ", sum)
    for i in range(len):
        for j in range(i, len):
            if (x[i] + x[j]) == sum:
                print(x[i], x[j])
sumlist(x,sum,len(x))                

