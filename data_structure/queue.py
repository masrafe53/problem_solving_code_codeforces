queue = []

def enqueue():
    a = input("Enter Element for add : ")
    queue.append(a)
    print(queue)
def dequeue():
    if not queue:
        print("Empty")
    else:
        e = queue.pop(0)
        print("Removing element is: ",e)
        
        
while True:
    print("! for add , 2 for delete")
    x = int(input())
    if x == 1:
        enqueue()
    elif x == 2:
        dequeue()