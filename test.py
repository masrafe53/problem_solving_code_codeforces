a = int(input())
for i in range(a):
      b = int(input())
      x = input()
      for j in range(1,len(x)):
            if x[j] in x[:j] and x[j] != x[j-1]:
                  print("No")
                  break
      else:
            print("Yes")