import re
s="pet:cat i love cats"
m=re.match(r'pet:\w\w\w',s)
print(m.group(0))
if m:
    print('match')
else:
    print('no match')    