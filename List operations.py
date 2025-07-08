l=[]
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice=input("Enter choice: ")
	if choice=="1":
		n=input("Integer: ")
		if n.isdigit():
			n1=int(n)
			l.append(n1)
			print("List after adding:", l)
		else:
			print("Invalid input")
	elif choice=="2":
		if l:
			n=input("Integer: ")
			if n.isdigit():
				n1=int(n)
				if n1 in l:
					l.remove(n1)
					print("List after removing:", l)
				else:
					print("Element not found")
			else:
				print("Invalid input")
		else:
			print("List is empty")
	elif choice=="3":
		if l:
			print(l)
		else:
			print("List is empty")
	elif choice=="4":
		break
	else:
		print("Invalid choice")
