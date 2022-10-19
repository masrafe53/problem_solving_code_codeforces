f,h = map(int, input().split())
a = list(map(int,input().split()))
result = 0
re = 0
for i in a:
    if i <= h:
        result = result + 1
    elif i > h :
        re = re+2
print(result+re)
    