t=int(input())
for t1 in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    ans=0
    red=len(l)-len(s)
    if(red%2!=0):
        ans-=1 
    print(ans+len(s))