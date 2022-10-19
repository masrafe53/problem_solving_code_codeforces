def my(arr,first,second,x):
    if first<=second:
        mid = (first+second)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid] > x:
            return my(arr, first,mid - 1, x)
        else:
            return my(arr, mid + 1, second, x)
    else:
        return -1
    
arr = list(map(int, input().split()))
x = int(input())
result = my(arr,0,len(arr)-1, x)
print("the number of index: ",result)
                