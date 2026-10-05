import heapq
start = (
    2, 8, 3,
    1, 6, 4,
    0, 7, 5
)
goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)
def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def astar(start, goal):

    pq = []

    g = 0
    h = heuristic(start)
    f = g + h

    heapq.heappush(pq, (f, g, start))

    cost = {
        start: 0
    }

    while pq:

        f, g, current = heapq.heappop(pq)

        if current == goal:
            return g

        zero = current.index(0)

        row = zero // 3
        col = zero % 3

        moves = [
            (-1, 0),   
            (1, 0),    
            (0, -1), 
            (0, 1)     
        ]

        for dr, dc in moves:

            new_row = row + dr
            new_col = col + dc

     
            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_zero = new_row * 3 + new_col

                new_state = list(current)
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)
                new_g = g + 1
                if new_state not in cost or new_g < cost[new_state]:

                    cost[new_state] = new_g

                    new_h = heuristic(new_state)
                    new_f = new_g + new_h

                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state)
                    )

    return -1



print("Initial State:")
print_state(start)

print("Goal State:")
print_state(goal)

print("Initial Heuristic =", heuristic(start))

result = astar(start, goal)

print("Goal Cost =", result)
