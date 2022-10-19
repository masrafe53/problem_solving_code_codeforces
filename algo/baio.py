def baio(arr,fst,last,x):
    if last >= fst :
        mid = (fst+last)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x :
            return baio(arr, fst, mid-1, x)
        else:
            return baio(arr, fst, mid + 1, x)
    else:
        return -1
arr = list(map(int,input().split()))
x = int(input())

result = baio(arr,0,len(arr)-1,x)
print(result)
    