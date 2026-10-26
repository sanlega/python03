import sys


def print_data() -> None:
    print("=== Command Quest ===")
    print(f"Command name: {sys.argv[0]}")
    args = sys.argv[1:]
    if len(args) > 0:
        print(f"Arguments received: {len(args)}")
        i = 1
        for a in args:
            print(f"Argument {i}: {a}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print_data()
