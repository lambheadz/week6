import re
txt = input()
x = r'[a-z]+_[a-z]+'
pt = re.search(x, txt)
if pt is not None:
    print(pt)
else:
    print('wrong')
"""   
import re
txt = input()
x = re.compile('[a-z]+_[a-z]+')
pt = x.search(txt)
if pt is not None:
    print(pt)
else:
    print('wrong')
"""