def bio(arr,x):
    low = 0
    hight = len(arr) - 1
    mid = 0
    
    while low <= hight:
        mid = (low+hight)//2
        if mid < x :
            hight = mid +1
        elif mid > x :
            low = mid -1
        else:
            return mid
arr = list(map(int,input().split()))
x = int(input())
result = bio(arr, x)
print(result)