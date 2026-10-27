import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print("")

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]

    print(f"Initial list of players: {players}")

    capitalized: list = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    only_capitalized: list = [
        name for name in players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalized}")
    print("")

    scores: dict = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    average: float = sum([scores[name] for name in scores]) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores: dict = {
        name: scores[name] for name in scores if scores[name] > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
