x = int(input())
for i in range(x):
    ans = 0
    a = list(map(int,input().split()))
    for i in a:
        if a[0] < i:
            ans = ans +1
    print(ans)
            
    
        
    
    