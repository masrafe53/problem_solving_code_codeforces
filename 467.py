a = int(input())
result = 0
for i in range(a):
    p,q = map(int,input().split())
    if p+2 <= q:
        result = result+1
print(result)