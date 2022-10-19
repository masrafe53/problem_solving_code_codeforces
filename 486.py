a = int(input())
a1 = count(a)
plus = 0
minus = 0
for i in range(a):
    x = int(input())
    if x % 2 ==0:
        plus = plus+1
    else:
        minus = minus+1
if plus % 2 == 0:
    pass
elif plus % 2 !=0:
    plus=plus // 2
    
if minus % 2 == 0:
    pass
elif minus % 2 !=0:
    minus=minus // 2
print(plus+minus)