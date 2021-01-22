def average(array):
    # your code goes here
    summ = sum(set(array))
    lenth = len(set(array))
    return summ/lenth

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
