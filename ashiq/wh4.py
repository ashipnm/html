s=str(input("enter a string:"))
rev=''
length=len(s)-1
while length>=0:
    rev=rev+s[length]
    length=length-1
print(rev)    