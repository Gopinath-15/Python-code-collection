ages = {}  


num_entries = int(input("How many people do you want to add? "))

for _ in range(num_entries):
    name = input("Enter person's name: ")
    age = int(input(f"Enter {name}'s age: "))
    ages[name] = age

print("\nAges you entered:")
for name, age in ages.items():
    print(f"{name} is {age} years old")
