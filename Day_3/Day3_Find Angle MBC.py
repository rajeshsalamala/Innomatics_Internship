# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = int(input())
bc = int(input())

h = (math.sqrt(ab**2 + bc**2))/2

adj = bc/2.0

Output = int(round(math.degrees(math.acos(adj/h))))

Output = str(Output)

print(Output+"°")
