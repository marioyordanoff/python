first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]

full_names = [f"{first.capitalize()} {last.capitalize()}" for first, last in zip(first_names, sur_names)]

print(full_names)