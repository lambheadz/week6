import re
txt = input()
x = r'[A-Z]+[a-z]+'
pt = re.search(x, txt)
if pt is not None:
    print(pt)
else:
    print('wrong')