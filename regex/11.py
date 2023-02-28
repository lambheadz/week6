import re
camel = input()
snake = re.sub(r'(?<!^)(?=[A-Z])', '_', camel)
print(snake.lower())