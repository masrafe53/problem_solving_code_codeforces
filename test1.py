T = int(input())
for i in range(T):
    N = int(input())
    x = [int(x) for x in input().split()]
    x  = x[::-1]
    sum = 0
    sign = 1
    for element in x:
        sum = sum + (element*element*sign)
      
        sign = sign * -1
    print(sum)