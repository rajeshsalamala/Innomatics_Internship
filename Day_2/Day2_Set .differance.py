# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT


english = int(input())
english_rollnumber = set(input().split())

frech = int(input())
french_rollnumbers = set(input().split())

print(len(english_rollnumber.difference(french_rollnumbers)))
