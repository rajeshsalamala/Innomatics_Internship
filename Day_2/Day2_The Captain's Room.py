N = int(input())

storage = sorted(map(int, input().split()))
total_rooms = len(storage)

for x in range(total_rooms):
    if(x != (total_rooms-1)):
        if(storage[x]!=storage[x-1] and storage[x]!=storage[x+1]):
            print(storage[x])
            break;
    else:
        print(storage[x])
