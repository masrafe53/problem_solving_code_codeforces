a = int(input())
for i in range(a):
    rating = int(input())
    
if 1900 <= rating:
    print("Division 1")
elif 1600<=rating<=1899:
    print("Division 2")
elif 1400<=rating<=1599:
    print("Division 3")
elif rating<=1399:
    print("Division 3")