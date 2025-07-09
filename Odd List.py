a=input()
b=list (map(int,a.split(',')))
for i in range (len(b)):
	if(b[i]%2 == 0):
		b[i] = b[i]+1
print(b)
