import re
import os.path

os.chdir("test")
data = os.listdir()

for i in data:
    if os.path.isfile(i) and (os.path.splitext(i))[1] == '.log':
        with open(i, 'r') as fo:
            text = fo.read()
            print(text)
pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'



# if re.search(pattern, text):
#     print('found a match')
# else:
#     print('no match')

matches =  re.findall(pattern, text)  # Ignore case
for i in  matches:
    print(i)
#
# matches = re.search(pattern, text)
# for match in matches:
#     # print ('found a match')
#     print(match.start(), match.end(), text[match.start():match.end()])
