arr = []

def adding():
    a = input("Enter your Element : ")
    arr.append(a)
    print(arr)
def deleteing():
    if not arr:
        print("No element is here ")
    else:
        arr.pop()
        print(arr)
while True:
    print(" Press 1 for adding, Press 2 for deleting")
    s = int(input())
    if s == 1:
        adding()
    elif s==2:
        deleteing()