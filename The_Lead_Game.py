a = int(input())
for i in range(a):
    x,y = map(int,input().split())
    ans = []
    v = x -y
    ans.append(v)
    ut = ans.sort()
    print(ans[-1])
    