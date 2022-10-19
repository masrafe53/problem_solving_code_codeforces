for _ in range(int(input())):
    l,r=[int(x) for x in input().split()]
    if l*2<=r:
        print(l,l*2)
    else:
        print(-1,-1)