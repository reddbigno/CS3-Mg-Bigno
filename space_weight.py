def calculate_space_weight(earth_weight: float, destination: str) -> float | str:
    space_weight = 0

    if destination == "mars":
        space_weight = earth_weight * 0.38
    elif destination == "jupiter":
        space_weight = earth_weight * 2.34
    elif destination == "moon":
        space_weight = earth_weight * 0.16
    else:
        return "Error. Planet unreachable"

    return space_weight


print(calculate_space_weight(75, "uranus"))
