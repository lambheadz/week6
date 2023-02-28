import re
txt = input()
x = re.split("[A-Z]", txt)
if x is not None:
    print(x)
else:
    print('enter a new string')