# password valid or not using reg ex
import re
s=input("enter a password:")
p="[a-z,A-Z]+[@][0-9]+"
password=re.findall(p,s)
if (password):
    print("valid password")
else:
    print("not valid")    