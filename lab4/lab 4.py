def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def hill_climbing():
    n = 4

    # Initial configuration from Week-4 PPT
    state = [3, 1, 2, 0]

    visited = {tuple(state)}

    while True:
        current_cost = calculate_cost(state)

        print("\nCurrent State:", state)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("Goal Reached!")
            break

        best_state = None
        best_cost = float('inf')

        print("\nNeighbor States:")

        for col in range(n):
            for row in range(n):
                if row != state[col]:

                    neighbor = state[:]
                    neighbor[col] = row

                    if tuple(neighbor) in visited:
                        continue

                    cost = calculate_cost(neighbor)

                    print(neighbor, "Cost:", cost)

                    if cost < best_cost:
                        best_cost = cost
                        best_state = neighbor

        # Stop if no unvisited neighbor is available
        if best_state is None or best_cost > current_cost:
            print("No better neighbor found!")
            break

        print("\nSelected Neighbor:", best_state)
        print("Selected Cost:", best_cost)

        state = best_state
        visited.add(tuple(state))

    print("\nFinal Configuration:", state)
    print("Final Cost:", calculate_cost(state))


hill_climbing()
