a = int(input())
for i in range(a):
    c = int(input())
    x = input()
    x1 = x.lower()
    n = 'timur'
    
    
    if len(n) != len(x):
        print("NO") 
    else:
    
        if x[0] == 'T' or x[1] == 'T' or x[2] == 'T' or x[3] == 'T' or x[4] == 'T'  and x1 == n:
            print('YES')
        
    
        else:
            print("NO")