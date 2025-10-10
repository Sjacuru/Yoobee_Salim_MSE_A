''' TOP-DOWN IMPLEMENTATION'''
# 1. SETUP THE GAME STATE

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
current_player = 'X'
game_running = True
winner = None

print("--- Tic-Tac-Toe! ---")

while game_running:
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

    print(f"Player {current_player}'s turn. Choose a spot (1-9): ")
    
    # Input validation loop
    valid_move = False
    while not valid_move:
        try:
            position = int(input()) - 1  # Convert to 0-indexed position
            
            # Check if position is valid (0-8) and spot is not taken
            if 0 <= position <= 8 and board[position] != 'X' and board[position] != 'O':
                board[position] = current_player
                valid_move = True
            elif 0 <= position <= 8:
                print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-9).")
    
    # Check for WIN
    win = False
    # Check Rows
    if board[0] == board[1] == board[2]: win = True
    elif board[3] == board[4] == board[5]: win = True
    elif board[6] == board[7] == board[8]: win = True
    # Check Columns
    elif board[0] == board[3] == board[6]: win = True
    elif board[1] == board[4] == board[7]: win = True
    elif board[2] == board[5] == board[8]: win = True
    # Check Diagonals
    elif board[0] == board[4] == board[8]: win = True
    elif board[2] == board[4] == board[6]: win = True

    if win:
        winner = current_player
        game_running = False
    
    # Check for TIE
    elif all(spot == 'X' or spot == 'O' for spot in board):
        game_running = False

    if game_running: # switch while the game is stil running
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# show final move
print("\n")
print(" " + board[0] + " | " + board[1] + " | " + board[2])
print("---|---|---")
print(" " + board[3] + " | " + board[4] + " | " + board[5])
print("---|---|---")
print(" " + board[6] + " | " + board[7] + " | " + board[8])
print("\n")

if winner is not None:
    print(f"Game Over! Player {winner} wins!")
else:
    print("Game Over! It's a tie.")
