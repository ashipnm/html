import re
txt="cat mat pat sat rat "
x=re.findall(r'[cmr]at',txt)
print(x)
