password=input("enter a password:")
upper=0
lower=0
length=0

if len(password)>= 8:
    length = True
    
    for letter in password:
        if letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
        elif letter.isdigit():
            digit = True
            


if length and lower and upper and digit:
    print('That is a valid password.')
else:
    print('That password is not valid.')