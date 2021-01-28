# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())

print_format = [('.|.'*(2*i+1)).center(m,'-') for i in  range(n//2)]

print('\n'.join(print_format+['WELCOME'.center(m,'-')]+print_format[::-1]))
