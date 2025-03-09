



from collections import deque

def water_jug_dfs(jug1, jug2, cap1, cap2, target, visited, path):
    if jug1 == target or jug2 == target:
        print("Solution Found:")
        for step, state in path:
            print(f"Rule {step}: {state}")
        return True

    if (jug1, jug2) in visited:
        return False

    visited.add((jug1, jug2))

    possible_moves = [
        (1, (cap1, jug2)),  # Fill Jug1
        (2, (jug1, cap2)),  # Fill Jug2
        (3, (0, jug2)),     # Empty Jug1
        (4, (jug1, 0)),     # Empty Jug2
        # Pour Jug1 -> Jug2
        (5, (jug1 - min(jug1, cap2 - jug2), jug2 + min(jug1, cap2 - jug2))),
        # Pour Jug2 -> Jug1
        (6, (jug1 + min(jug2, cap1 - jug1), jug2 - min(jug2, cap1 - jug1)))
    ]

    for rule, (new_jug1, new_jug2) in possible_moves:
        if (new_jug1, new_jug2) not in visited:
            if water_jug_dfs(new_jug1, new_jug2, cap1, cap2, target, visited, path + [(rule, (new_jug1, new_jug2))]):
                return True

    return False

def solve_water_jug(cap1, cap2, target):
    visited = set()
    if not water_jug_dfs(0, 0, cap1, cap2, target, visited, [(0, (0, 0))]):
        print("No solution found")

# Example execution
solve_water_jug(4, 3, 2)

