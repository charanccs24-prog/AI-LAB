import random
import math

def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def simulated_annealing():
    n = 8

    for restart in range(100):
        state = [random.randint(0, n - 1) for _ in range(n)]

        temperature = 10.0
        cooling_rate = 0.995

        while temperature > 0.001:
            current_cost = calculate_cost(state)

            if current_cost == 0:
                print("Solution Found!")
                print("Final State:", state)
                print("Cost:", current_cost)

                for row in range(n):
                    for col in range(n):
                        if state[col] == row:
                            print("Q", end=" ")
                        else:
                            print(".", end=" ")
                    print()

                return

            neighbor = state[:]

            col = random.randint(0, n - 1)
            row = random.randint(0, n - 1)

            while row == neighbor[col]:
                row = random.randint(0, n - 1)

            neighbor[col] = row

            new_cost = calculate_cost(neighbor)
            delta = new_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                state = neighbor

            temperature *= cooling_rate

    print("Solution not found. Try again.")


simulated_annealing()
