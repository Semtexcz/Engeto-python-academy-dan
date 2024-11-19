import csv
import random

# Data for the generation
names = ["Jan", "Petra", "Marek", "Lucie", "Eva", "Tomas", "Katerina", "Jiri", "Pavel", "Anna"]
cities = ["Brno", "Praha", "Ostrava", "Plzen", "Olomouc"]

# Generate random data
data = []
for _ in range(50):  # Generate 50 records
    name = random.choice(names)
    age = random.randint(20, 60)
    city = random.choice(cities)
    income = round(random.uniform(1000, 3000), 2)  # Random income between 1000 and 3000 EUR
    data.append({"jmeno": name, "vek": age, "mesto": city, "prijem": income})

# Write to CSV file
filename = "salaries.csv"
with open(filename, mode="w", newline="") as file:
    fieldnames = ["jmeno", "vek", "mesto", "prijem"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Data byla úspěšně vygenerována a uložena do souboru {filename}.")