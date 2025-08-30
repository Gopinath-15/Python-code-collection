g=input()
h=list (map(int,g.split(',')))
for i in range (len(h)):
	if(h[i]%2 == 0):
		h[i] = h[i]+1
print(h)
