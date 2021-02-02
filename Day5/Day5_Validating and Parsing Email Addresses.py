import re
n = int(input())

for i in range(n):
    x, y = input().split()
    pattern = "<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if re.match(pattern,y):
        print(x,y)
    else:
        pass
    
