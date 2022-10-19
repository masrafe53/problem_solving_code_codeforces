a= int(input())
for i in range(a):
    a = int(input())
    ans = ''
    for i in range(9,1,-1):
        if a>i:
            ans = ans+str(i)
            a = a - i
        else:
            break
    ans = str(a)
    print(ans[::-1])
        
    