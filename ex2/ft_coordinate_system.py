import math


def get_player_pos():
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        values = coordinates.split(",")

        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(values[0])
            y = float(values[1])
            z = float(values[2])
            return (x, y, z)
        except ValueError as error:
            print(f"Invalid coordinates: {error}")


def calc_distance(first: tuple, second: tuple) -> float:
    res: float = math.sqrt((second[0] - first[0])**2 +
                           (second[1] - first[1])**2 +
                           (second[2] - first[2])**2)
    return res


def distance() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first: tuple = get_player_pos()
    print(
        f"Got a first tuple: ({first[0]:.1f},"
        f"{first[1]:.1f}, {first[2]:.1f})"
    )
    print(f"It includes: X={first[0]:.1f}, Y={first[1]:.1f}, Z={first[2]:.1f}")
    print(
        "Distance to center: "
        f"{math.sqrt(first[0]**2 + first[1]**2 + first[2]**2):.4f}"
    )
    print("")

    print("Get a second set of coordinates")
    second: tuple = get_player_pos()
    calc: float = calc_distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {calc:.4f}")


if __name__ == "__main__":
    distance()
