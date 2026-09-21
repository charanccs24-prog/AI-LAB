def print_board(board):
    """Utility to print a well-formatted tic-tac-toe grid."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board):
    """Checks the game status. Returns 'X', 'O', 'Tie', or None."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != " ":
            return board[cond[0]]
    if " " not in board:
        return "Tie"
    return None

def print_path(path):
    """Formats and prints a single completed state sequence from start to finish."""
    print("➡️ NEW STATE SPACE PATH:")
    for step, board in enumerate(path):
        print(f"Step {step}:")
        print_board(board)
    print("=" * 40)

def generate_state_space(current_board, current_player, current_path):
    """Recursively traverses the remaining grid choices via Depth-First Search (DFS)."""
    new_path = list(current_path) + [copy.deepcopy(current_board)]
    
    status = check_winner(current_board)
    if status:
        print_path(new_path)
        print(f"Outcome of this branch: {f'Winner is {status}' if status != 'Tie' else 'It is a Tie!'}\n")
        return

    next_player = "O" if current_player == "X" else "X"
    for i in range(9):
        if current_board[i] == " ":
            current_board[i] = current_player
            generate_state_space(current_board, next_player, new_path)
            current_board[i] = " " 

def get_initial_board():
    """Asks the user for exactly 6 initial inputs to populate the grid."""
    board = [" "] * 9
    print("--- Tic-Tac-Toe Position Guide ---")
    print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")
    
    filled_count = 0
    players = ["X", "O"] 
    
    while filled_count < 6:
        active_player = players[filled_count % 2]
        try:
            pos = int(input(f"Enter index (0-8) to place '{active_player}' [{filled_count + 1}/6]: "))
            if pos < 0 or pos > 8:
                print("❌ Out of bounds! Choose an index from 0 to 8.")
                continue
            if board[pos] != " ":
                print("❌ Position already filled! Choose a vacant index.")
                continue
            
            board[pos] = active_player
            filled_count += 1
            print_board(board)
        except ValueError:
            print("❌ Invalid input! Please type an integer from 0 to 8.")
            
    return board, players[filled_count % 2]

if __name__ == "__main__":
    print("--- STEP 1: SETUP YOUR 6 PRE-FILLED PLACES ---")
    initial_board, next_up = get_initial_board()
    
    print("\n--- STEP 2: GENERATING ALL VALID STATE SPACE PATHS ---")
    generate_state_space(initial_board, next_up, [])
