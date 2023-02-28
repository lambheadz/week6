import re
txt = input()
x = r'\ba.*\wb$'
pt = re.search(x, txt)
if pt is not None:
    print(pt)
else:
    print('wrong')