def gen_player_achievements():
    alice = {'Crafting Genius', 'World Savior', 'Master Explorer',
             'Collector Supreme', 'Untouchable', 'Boss Slayer'}
    print(f"Player Alice: {alice}")
    bob = {'Crafting Genius', 'Strategist', 'World Savior',
           'Master Explorer', 'Unstoppable',
           'Collector Supreme', 'Untouchable'}
    print(f"Player Bob: {bob}")
    charlie = {'Strategist', 'Speed Runner', 'Survivor',
               'Master Explorer', 'Treasure Hunter',
               'First Steps', 'Collector Supreme',
               'Untouchable', 'Sharp Mind'}
    print(f"Player Charlie: {charlie}")
    dylan = {'Strategist', 'Speed Runner', 'Unstoppable',
             'Untouchable', 'Boss Slayer'}
    print(f"Player Dylan: {dylan}")
    print("")
    all_achievents = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievents}")
    intersection = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {intersection}")

    only_alice = alice - (bob | charlie | dylan)
    print(f"Only Alice has: {only_alice}")
    only_bob = bob - (alice | charlie | dylan)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie - (alice | bob | dylan)
    print(f"Only charlie has: {only_charlie}")
    only_dylan = dylan - (alice | bob | dylan)
    print(f"Only Dylan has: {only_dylan}")
    print("")

    alice_diff = all_achievents - alice
    print(f"Alice is missing: {alice_diff}")
    bob_diff = all_achievents - bob
    print(f"Bob is missing: {bob_diff}")
    charlie_diff = all_achievents - charlie
    print(f"Charlie is missing: {charlie_diff}")
    dylan_diff = all_achievents - dylan
    print(f"Dylan is missing: {dylan_diff}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")
    gen_player_achievements()
