def dfs(start, goal):
    # Stack contains: (state, level)
    stack = [(start, 0)]
    visited = set()

    while stack:
        state, level = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        # Goal reached
        if state == goal:
            return level

        blank = state.index(0)

        row = blank // 3
        col = blank % 3

        moves = []

        if row > 0:
            moves.append(blank - 3)   # Up

        if row < 2:
            moves.append(blank + 3)   # Down

        if col > 0:
            moves.append(blank - 1)   # Left

        if col < 2:
            moves.append(blank + 1)   # Right

        for new_pos in moves:
            new_state = list(state)

            new_state[blank], new_state[new_pos] = \
                new_state[new_pos], new_state[blank]

            new_state = tuple(new_state)

            if new_state not in visited:
                stack.append((new_state, level + 1))

    return -1


def print_board(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])


# Initial State
start = (
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
)

# Goal State
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

print("Initial State:")
print_board(start)

print("\nGoal State:")
print_board(goal)

# DFS
goal_cost = dfs(start, goal)

if goal_cost != -1:
    print("\nSolution Found")
    print("Goal Cost:", goal_cost)
    print("charan c 1WN24CS069")
else:
    print("\nNo solution found")
