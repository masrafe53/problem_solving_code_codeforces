n = int(input())
for i in range(n):
    s = int(input())
    ans = ''
    for i in range(9, 1, -1):
        if s > i:
            ans = ans + str(i)
            s = s-i
        else: break
    ans = ans + str(s)
    print(ans[::-1])