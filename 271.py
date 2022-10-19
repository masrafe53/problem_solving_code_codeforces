a = input()
b = 0
ans = 0
for i in a:
    if a[-1] == b:
        b = b+1
        if b[-1] != a[-1]:
            ans = ans+0
            print(ans)
            