def calculate_fuel(cargo_weight):
    final_fuel = 0
    base_ship_weight = 50000
    total_weight = cargo_weight + base_ship_weight
    final_fuel = total_weight * 3

    return final_fuel


is_loading = True
total_cargo_weight = 0

while is_loading:

    user_input = input("Choose from the available cargo to load: \n" +
                       "1. Satellite \n" +
                       "2. Rover \n" +
                       "3. Supplies \n" +
                       "Your choice: ")

    if user_input == "launch":
        break

    if user_input == "satellite":
        total_cargo_weight += 1000
        print("Satellite is loaded")
    elif user_input == "rover":
        total_cargo_weight += 2500
        print("Rover is loaded")
    elif user_input == "suppplies":
        total_cargo_weight += 500
        print("Supplies are loaded")
    else:
        print("The item is not approved for the mission")

    print("\n Current cargo weight: ", total_cargo_weight)

    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED")
        is_loading = False

print("Total cargo weight: ", total_cargo_weight)
print("Final fuel needed: ", calculate_fuel(total_cargo_weight))
