# 1.abd abcd
# 2.abcd abccd abcccd abccccd  ab.+d
# 3.abd abcd abccd abcccd abccccd ab.*d
# 4.abccd ab.{2}d
import re
s='abd abcd abccd abcccd abccccd'
x=re.findall('ab.?d',s)
# x=re.findall('ab.+d',s)
# x=re.findall('ab.*d',s)
# x=re.findall('ab.{2}d',s)
print(x)