# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()
for i in range(int(n)):
    m = input()
    print(bool(re.match(r'^[+-]?\d*\.\d+$',m)))
