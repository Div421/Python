import re
import os.path

os.chdir("test")
data = os.listdir()

for i in data:
    if os.path.isfile(i) and (os.path.splitext(i))[1] == '.log':
        with open(i, 'r') as fo:
            text = fo.read()
            print(text)