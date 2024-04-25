data = {
    "Bansko": 97,
    "Brussels": 1701,
    "Alexandria": 1403,
    "Nice": 1307,
    "Szeged": 469,
    "Dublin": 2479,
    "Palermo": 987,
    "Moscow": 1779,
    "Oslo": 2098,
    "London": 2019,
    "Madrid": 2259
}

print("Distances below 1500 km from Sofia are:")
for city, distance in data.items():
    if distance < 1500:
        print(f"{city} - {distance}")