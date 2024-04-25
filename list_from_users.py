num_names = int(input("How many names are you going to enter: "))

names = []

for i in range(num_names):
    name = input("Enter a name,please:")
    names.append(name)


print("The names you have entered are:")
for name in names:
    print(name)