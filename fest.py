for i in range(int(input())):
    n,x,y = map(int, input().split())
    ex = (n+1)//2
    ey = ex
    result = 1
    if x%2==0 and y%2==0:
        result = 0
    elif x%2==1 and y%2==1:
        result=0
    print(result)