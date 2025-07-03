a=input(("Enter the elements of the list: ")) #getting the input
b=list(map(int,a.split(',')))
c=sorted(b)
d=sorted(b,reverse=True)
print("Ascending order: ", c)
print("Descending order: ",d)
