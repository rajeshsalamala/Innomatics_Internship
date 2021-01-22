if __name__ == '__main__':
    N = int(input())
    lis = [];
    for x in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(lis)
        elif ip[0] == "insert":
            lis.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            lis.remove(int(ip[1]))
        elif ip[0] == "pop":
            lis.pop();
        elif ip[0] == "append":
            lis.append(int(ip[1]))
        elif ip[0] == "sort":
            lis.sort();
        else:
            lis.reverse();
