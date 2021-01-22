# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

countries = set()
if 0<n<1000:

    for x in range(n):
        countries.add(input())
    print(len(countries))
