n=int(input())
p=0
l=list()
for i in range (n):
    a,b=map(int,input().split())
    p=p-a
    p=p+b
    l.append(p)
print(max(l))