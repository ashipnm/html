i=2
num = int(input('Enter a number'))
flag=1

while i < num:
    if(num % i) == 0:
        flag = 0
    i = i+1
    
if flag:
    print('Number is a Prime Number')
else:
    print('Number  is not a Prime Number')