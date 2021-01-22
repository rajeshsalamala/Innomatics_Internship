n = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    ip = input().split()
    s = set(map(int,input().split()))
    if (ip[0] == 'update'):
        a |= s
    elif (ip[0] == 'intersection_update'):
        a &= s
    elif (ip[0] == 'difference_update'):
        a -= s
    elif (ip[0] == 'symmetric_difference_update'):
        a ^= s
print(sum(a))
