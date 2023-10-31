ctemps = [35,10,50,88]
for c in ctemps:
    f = ((9 * float(c)) / 5) + 32
    print(f"Celcius {c} is Fahrenheit {f}")

fruits = ["Apples ", "Bananas ", "Oranges "]

clean_fruits = [f.lower().strip() for f in fruits]

for f in clean_fruits:
    print(f)