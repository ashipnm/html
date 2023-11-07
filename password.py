password=input("enter a password:")
length=0
Upper=0
Lower=0
Digit=0
if len(password)>=8:
    length=1
    for letter in password:
        if letter.isdigit():
            Digit=1
        elif letter.isupper():
            Upper=1 
        elif letter.islower():
            Lower=1
if length and Upper and Lower and Digit: 
    print("Valid Password.")
else:
    print("Invalid Password.")               
   
