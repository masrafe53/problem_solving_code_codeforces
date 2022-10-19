t=int(input())
for i in range(t):
	n = int(input())
	s = input()
	for j in range(1,len(s)):
		if s[j] in s[:j] and s[j]!=s[j-1]:
			print("NO")
			break
	else:
		print("YES")