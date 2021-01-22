# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())


for _ in range(t):

    a = int(input())
    a_space = set(input().split())

    b = int(input())
    b_space = set(input().split())

    print(a_space.issubset(b_space))
