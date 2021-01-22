# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
n = int(input())
output = True

for x in range(0,n):
    a2 = set(input().split())

    if not a2.issubset(a):
        output = False

    if len(a2) >= len(a):
        output = False
print(output)
        
