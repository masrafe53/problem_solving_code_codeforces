a = int(input())
for i in range(a):
    x = int(input())
    y = list(map(int,input().split()))
    y.sort()
    x = 0
    for i in range(y-2):
        if y[i] == y[i+1] == y[i+2]:
            x = y[i]
            break
    if x != 0:
        print(y[i])
    else:
        print(-1)