def linear(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = list(map(str,input().split()))
x = input()
result = linear(arr, x)
print(result)