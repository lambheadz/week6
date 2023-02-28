import re
snake = input()
camel = ''.join(x.capitalize() or '_' for x in snake.split('_'))
print(camel)