d=int(input("Enter number of Days:"))
if d==30:
    print("April,June,September,November")
elif d==31:
    print("January,March,May,July,August,October,December")    
elif d==28:
    print("February")
else:
    print("Invalid Month")
            