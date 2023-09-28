a=input("enter the string:")
y=a.split()
s=''
for i in y:
    x=i[::-1]
    if i.lower()==x.lower():
    # print("@" * len(i))
     s+="@"*len(i)
    else:
     s+=i
print(s)
#output
  # palindrome convert each character which @
  # y  dad said our mother toungue is malayalam
  #my  @@@ said our mother toungue is @@@@@@@@@
  
