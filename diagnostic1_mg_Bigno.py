def calculate_space_weight(earth_weight, destination):
    if destination == "mars":
       earth_weight = earth_weight * 0.38
       return earth_weight
    elif destination == "jupiter":
        earth_weight = earth_weight * 2.34
        return earth_weight
    elif destination == "moon":
        earth_weight = earth_weight * 0.16
        return earth_weight
    else:
        print("Enter a valid destination (mars, jupiter, moon)")
        return 0

def main():
    earth_weight = float(input("Enter your earth weight: "))
    destination = str(input("Enter your destination (mars, jupiter," \
    "moon): "))
    print(calculate_space_weight(70, "mars"))

main()

