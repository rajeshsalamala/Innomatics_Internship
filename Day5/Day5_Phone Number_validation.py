import re
for i in range(int(input())):
    number = input()
    if (len(number)==10) and (number.isdigit()):
        res = re.findall(r'^[789]\d{9}',number)
        if res:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
