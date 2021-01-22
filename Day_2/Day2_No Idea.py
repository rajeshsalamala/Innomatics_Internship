# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split()
m = int(a[0])
n = int(a[1])
lis = []
happyness = 0
lis = list(map(int, input().strip().split()))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for x in lis:
    if x in A:
        happyness = happyness+1
    if x in B:
        happyness = happyness-1

print(happyness)
