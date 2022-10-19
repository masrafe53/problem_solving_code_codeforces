a = str(input())
u = 0
l = 0
for i in range(len(a)):
    if (a[i]>='a' and a[i]<='z'):
        l = l+1
    elif (a[i]>='A' and a[i]<='Z'):
        u = u+1
if l>=u:
    print(a.lower())
elif l<u:
    print(a.upper())