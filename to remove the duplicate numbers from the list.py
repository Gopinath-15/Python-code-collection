a=input(("Enter the elements of the list: "))
b=list(map(int,a.split()))
seen = set()
c =[x for x in b if not (x in seen or seen.add(x))]
print (c)
