#practice
import re
txt = input()
x = re.search(r"\bc\wt\b", txt)
if x is not None:
    print("ok")
else:
    print("not ok")