from itertools import count


a = int(input())
for i in range(a):
    x,y = input().split()
    
    xX = x.count('X')
    yX = y.count('X')
    xS = x.count('S')
    yS = x.count('S')
    
    
    if x[-1] == 'L' and xX == yX :
        print('=')
    if x[-1] == 'L' and xX > yX:
        print('>')
    if x[-1] == 'L' and xX < yX:
        print('<')
    if x[-1] == 'S' and xS == yS:
        print('=')
    if x[-1] == 'S' and xS > yS:
        print('<')
    if x[-1] == 'S' and xS < yS:
        print('>')
    if x[0] == 'X' and y[0] != 'X':
        print('>')
    if x[0] != 'X' and y[0] == 'X':
        print('<')
    if x == 'L' and y == 'S':
        print('>')
    if x == 'S' and y == 'L':
        print('<')
        
           
