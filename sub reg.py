# replace the word from the string
# john@abc.com and mike@pgr.com
# ans:john@gmail.com and mike@gmail.com
import  re
s="john@abc.com and mike@pgr.com"
x=re.sub('abc|pgr','gmail',s)
print(x) 