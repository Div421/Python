import re
pattern = '^[0-9]{10}$'
text = input("Enter Mobile Number")


if re.search(pattern,text): #this none is converted to false by if condition
    print ('Valid')
else:
    print ('Invalid')