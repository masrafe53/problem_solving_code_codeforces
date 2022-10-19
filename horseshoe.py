a = list(map(int,input().split()))
b = len(a)
nodup = list(dict.fromkeys(a))
no = len(nodup)
sum = b-no
print(sum)
