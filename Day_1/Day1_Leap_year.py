def is_leap(year):
    leap = False

    # Write your logic here
    if year in range(1990, pow(10,5)):
        if year%400==0:
            leap = True
        elif year%100 == 0:
            leap =  False
        elif year%4 == 0:
            leap = True
        return leap

year = int(raw_input())
