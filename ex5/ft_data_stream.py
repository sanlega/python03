
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "release", "use"
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[tuple[str, str]]) -> Generator:
    while events:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for i in range(10):
        events += [next(generator)]

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
