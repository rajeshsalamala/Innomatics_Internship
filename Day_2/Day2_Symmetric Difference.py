# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input().strip())
set_m = set(map(int, input().strip().split(' ')))

N = int(input().strip())
set_n = set(map(int, input().strip().split(' ')))

for x in sorted(set_m ^ set_n):
    print(x)
