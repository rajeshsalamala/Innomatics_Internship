def swap_case(s):

    b = ""
    for x in s:
        if x.islower() == True:
            b+= (x.upper())
        elif x.isupper() == True:
            b += (x.lower())
        else:
            b+=(x)
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
