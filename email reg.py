# email is valid or not using  reg ex
import re
e=input("enter a email:")
m="[a-z]+[0-9]+[@][a-z]+[.][a-z]{3,2}"
email=re.findall(m,e)
if (email):
    print("valid email")
else:
    print("invalid email")    