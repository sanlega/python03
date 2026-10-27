import sys


def get_inventory() -> list:
    inventory = {}

    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, quantity = arg.split(":")

        if not item or not quantity:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(quantity)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    return inventory


def analyze_inventory(inventory) -> None:
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if total == 0:
        return

    most_item = None
    least_item = None

    for item in inventory:
        quantity: int = inventory[item]
        percentage: float = round(quantity / total * 100, 1)

        print(f"Item {item} represents {percentage:.1f}%")

        if most_item is None or quantity > inventory[most_item]:
            most_item = item

        if least_item is None or quantity < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict = get_inventory()
    analyze_inventory(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
