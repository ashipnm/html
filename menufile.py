# 1# create a file 
# f=open("f1.txt","r")
#2 # add anothera file
# f=open("f2.txt","w")
# f.write("\npython is a programming language")
# f.close()
# f=open("f2.txt","r")
# print(f.read())
# 3.delete file
# import os
# os.remove("f2.txt")
f=open("f1.txt","r")
f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("demofile2.txt", "r")
print(f.read())
import os
if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
else:
  print("The file does not exist")
# print(f.read())  

